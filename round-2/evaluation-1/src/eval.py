#!/usr/bin/env python3
"""Comprehensive evaluation of TF-ISF vs BM25 vs Cosine retrieval experiment results.

Loads per-example predictions from the iter_1 experiment (n=180, tencent/hy3:free),
then computes:
  - Pairwise F1 with bootstrap CIs and Holm-Bonferroni correction
  - Effect sizes: Cohen's d and Hedges' g
  - Per-example F1 statistics (mean/std/quartiles per method)
  - CI overlap test per pair
  - Subgroup analysis by gold section type
  - Hallucination rate (F1>0 with no evidence-section match)
  - Section recall stats
  - Variance decomposition via Kruskal-Wallis
  - Reliability ranking of the single available experiment
"""

import json
import sys
import math
import resource
import gc
from pathlib import Path
from collections import defaultdict

import numpy as np
from scipy import stats
from loguru import logger

# ── logging ──────────────────────────────────────────────────────────────────
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# ── memory limits ─────────────────────────────────────────────────────────────
RAM_LIMIT = 8 * 1024**3  # 8 GB (well within 29 GB container)
resource.setrlimit(resource.RLIMIT_AS, (RAM_LIMIT, RAM_LIMIT))

WORKSPACE = Path(__file__).parent
EXPERIMENT_1 = Path(
    "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT"
    "/3_invention_loop/iter_1/gen_art/gen_art_experiment_1"
)
METHODS = ["cosine", "bm25", "tf_isf"]
N_BOOTSTRAP = 10_000
RNG_SEED = 42


# ── helpers ───────────────────────────────────────────────────────────────────

def parse_f1(v) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def bootstrap_ci(
    arr: np.ndarray,
    n_boot: int = N_BOOTSTRAP,
    ci: float = 0.95,
    rng: np.random.Generator = None,
) -> tuple[float, float, float]:
    """Return (mean, lower_ci, upper_ci) via percentile bootstrap."""
    if rng is None:
        rng = np.random.default_rng(RNG_SEED)
    means = np.array([rng.choice(arr, size=len(arr), replace=True).mean() for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return float(arr.mean()), float(np.percentile(means, 100 * alpha)), float(np.percentile(means, 100 * (1 - alpha)))


def bootstrap_diff_ci(
    a: np.ndarray,
    b: np.ndarray,
    n_boot: int = N_BOOTSTRAP,
    ci: float = 0.95,
    rng: np.random.Generator = None,
) -> tuple[float, float, float, float]:
    """Return (diff, lower, upper, p_value) for paired mean difference a - b."""
    if rng is None:
        rng = np.random.default_rng(RNG_SEED)
    diff_obs = a.mean() - b.mean()
    diffs = np.array([
        rng.choice(a, size=len(a), replace=True).mean() -
        rng.choice(b, size=len(b), replace=True).mean()
        for _ in range(n_boot)
    ])
    alpha = (1 - ci) / 2
    lo = float(np.percentile(diffs, 100 * alpha))
    hi = float(np.percentile(diffs, 100 * (1 - alpha)))
    # two-sided p: fraction of bootstrap diffs with opposite sign to observed
    p_val = float(2 * min((diffs >= 0).mean(), (diffs <= 0).mean()))
    return float(diff_obs), lo, hi, p_val


def cohen_d(a: np.ndarray, b: np.ndarray) -> float:
    pooled_std = math.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2)
    if pooled_std == 0:
        return 0.0
    return float((a.mean() - b.mean()) / pooled_std)


def hedges_g(a: np.ndarray, b: np.ndarray) -> float:
    n1, n2 = len(a), len(b)
    d = cohen_d(a, b)
    # correction factor J
    df = n1 + n2 - 2
    j = 1 - (3 / (4 * df - 1))
    return float(d * j)


def ci_overlap_pct(lo1: float, hi1: float, lo2: float, hi2: float) -> float:
    """Percentage of CI width that overlaps. 0 means no overlap (significant)."""
    overlap = max(0.0, min(hi1, hi2) - max(lo1, lo2))
    width1 = hi1 - lo1
    width2 = hi2 - lo2
    avg_width = (width1 + width2) / 2
    if avg_width == 0:
        return 0.0
    return float(overlap / avg_width * 100)


def holm_bonferroni(p_values: list[float]) -> list[float]:
    """Return Holm-Bonferroni corrected p-values."""
    n = len(p_values)
    indexed = sorted(enumerate(p_values), key=lambda x: x[1])
    corrected = [0.0] * n
    prev = 0.0
    for rank, (orig_i, p) in enumerate(indexed):
        adj = min(1.0, max(prev, p * (n - rank)))
        corrected[orig_i] = adj
        prev = adj
    return corrected


def describe(arr: np.ndarray) -> dict:
    return {
        "n": int(len(arr)),
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=1)),
        "min": float(arr.min()),
        "q25": float(np.percentile(arr, 25)),
        "median": float(np.median(arr)),
        "q75": float(np.percentile(arr, 75)),
        "max": float(arr.max()),
    }


# ── main ──────────────────────────────────────────────────────────────────────

@logger.catch(reraise=True)
def main():
    rng = np.random.default_rng(RNG_SEED)

    # ── 1. Load experiment data ───────────────────────────────────────────────
    exp1_path = EXPERIMENT_1 / "full_method_out.json"
    logger.info(f"Loading {exp1_path}")
    raw = json.loads(exp1_path.read_text())
    examples = raw["datasets"][0]["examples"]
    n = len(examples)
    logger.info(f"Loaded {n} examples from iter_1 experiment")

    meta = raw.get("metadata", {})
    llm_model = meta.get("llm_model", "tencent/hy3:free")
    logger.info(f"LLM model: {llm_model}")

    # ── 2. Extract per-example F1 arrays ─────────────────────────────────────
    f1: dict[str, np.ndarray] = {}
    recall: dict[str, np.ndarray] = {}
    gold_types: list[str] = []
    retrieved_sections: dict[str, list[str]] = {m: [] for m in METHODS}
    answers: dict[str, list[str]] = {m: [] for m in METHODS}
    gold_answers: list[str] = []

    f1_lists: dict[str, list[float]] = {m: [] for m in METHODS}
    recall_lists: dict[str, list[float]] = {m: [] for m in METHODS}

    for ex in examples:
        gold_types.append(ex.get("metadata_gold_section_type", "Unknown"))
        gold_answers.append(ex.get("output", ""))
        for m in METHODS:
            f1_lists[m].append(parse_f1(ex.get(f"metadata_f1_{m}", 0)))
            recall_lists[m].append(parse_f1(ex.get(f"metadata_section_recall_{m}", 0)))
            retrieved_sections[m].append(ex.get(f"metadata_retrieved_sections_{m}", ""))
            answers[m].append(ex.get(f"predict_{m}_answer", ""))

    for m in METHODS:
        f1[m] = np.array(f1_lists[m])
        recall[m] = np.array(recall_lists[m])

    del raw, examples
    gc.collect()

    unique_types = sorted(set(gold_types))
    logger.info(f"Gold section types: {unique_types}")

    # ── 3. Per-example F1 descriptive statistics ──────────────────────────────
    logger.info("Computing descriptive statistics per method")
    desc_stats = {m: describe(f1[m]) for m in METHODS}
    for m in METHODS:
        logger.info(f"  {m}: mean={desc_stats[m]['mean']:.4f} std={desc_stats[m]['std']:.4f}")

    # ── 4. Bootstrap CIs per method ───────────────────────────────────────────
    logger.info("Computing bootstrap CIs per method")
    method_ci: dict[str, tuple] = {}
    for m in METHODS:
        mu, lo, hi = bootstrap_ci(f1[m], rng=rng)
        method_ci[m] = (mu, lo, hi)
        logger.info(f"  {m}: mean={mu:.4f} 95%CI=[{lo:.4f}, {hi:.4f}]")

    # ── 5. Pairwise comparisons with bootstrap + Holm-Bonferroni ─────────────
    logger.info("Computing pairwise F1 comparisons")
    pairs = [
        ("tf_isf", "cosine"),
        ("tf_isf", "bm25"),
        ("bm25", "cosine"),
    ]
    raw_p_values = []
    pair_results_raw = []
    for a, b in pairs:
        diff, lo, hi, p = bootstrap_diff_ci(f1[a], f1[b], rng=rng)
        raw_p_values.append(p)
        pair_results_raw.append({
            "pair": f"{a}_vs_{b}",
            "diff": diff,
            "ci_lo": lo,
            "ci_hi": hi,
            "p_raw": p,
            "cohen_d": cohen_d(f1[a], f1[b]),
            "hedges_g": hedges_g(f1[a], f1[b]),
            "ci_overlap_pct": ci_overlap_pct(*method_ci[a][1:], *method_ci[b][1:]),
            "significant_no_overlap": method_ci[a][2] < method_ci[b][1] or method_ci[b][2] < method_ci[a][1],
        })

    corrected_p = holm_bonferroni(raw_p_values)
    pairwise_comparisons = []
    for i, res in enumerate(pair_results_raw):
        res["p_holm_bonferroni"] = corrected_p[i]
        res["significant_hb_alpha05"] = corrected_p[i] < 0.05
        pairwise_comparisons.append(res)
        logger.info(
            f"  {res['pair']}: diff={res['diff']:+.4f} CI=[{res['ci_lo']:.4f},{res['ci_hi']:.4f}] "
            f"p_raw={res['p_raw']:.4f} p_hb={res['p_holm_bonferroni']:.4f} d={res['cohen_d']:.3f}"
        )

    # ── 6. Subgroup analysis by section type ──────────────────────────────────
    logger.info("Subgroup analysis by gold section type")
    subgroup_results: dict[str, dict] = {}
    gold_types_arr = np.array(gold_types)
    for stype in unique_types:
        mask = gold_types_arr == stype
        n_sub = int(mask.sum())
        if n_sub < 2:
            continue
        sub: dict[str, np.ndarray] = {m: f1[m][mask] for m in METHODS}
        sub_means = {m: float(sub[m].mean()) for m in METHODS}
        best_method = max(sub_means, key=sub_means.get)
        sub_pairs = []
        for a, b in pairs:
            if len(sub[a]) < 5:
                diff = float(sub[a].mean() - sub[b].mean())
                sub_pairs.append({"pair": f"{a}_vs_{b}", "diff": diff, "note": "too_few_for_bootstrap"})
            else:
                diff, lo, hi, p = bootstrap_diff_ci(sub[a], sub[b], rng=rng)
                sub_pairs.append({"pair": f"{a}_vs_{b}", "diff": diff, "ci_lo": lo, "ci_hi": hi, "p_raw": p})
        subgroup_results[stype] = {
            "n": n_sub,
            "means": sub_means,
            "best_method": best_method,
            "pairwise": sub_pairs,
        }
        logger.info(f"  {stype} (n={n_sub}): {sub_means} → best={best_method}")

    # ── 7. Hallucination rate ─────────────────────────────────────────────────
    logger.info("Computing hallucination rates")
    halluc: dict[str, dict] = {}
    for m in METHODS:
        halluc_count = 0
        for i in range(n):
            f1_val = f1[m][i]
            rec_val = recall[m][i]
            ans = answers[m][i]
            if f1_val > 0 and rec_val == 0 and len(ans.strip()) > 0:
                halluc_count += 1
        rate = halluc_count / n * 100
        halluc[m] = {"count": halluc_count, "rate_pct": rate}
        logger.info(f"  {m}: hallucination_count={halluc_count} ({rate:.1f}%)")

    # ── 8. Section recall stats ───────────────────────────────────────────────
    recall_stats = {m: describe(recall[m]) for m in METHODS}

    # ── 9. Kruskal-Wallis variance decomposition ──────────────────────────────
    logger.info("Kruskal-Wallis test across methods")
    kw_stat, kw_p = stats.kruskal(f1["cosine"], f1["bm25"], f1["tf_isf"])
    # eta-squared approximation for KW
    k = 3  # number of groups
    n_total = n * k
    kw_eta2 = (kw_stat - k + 1) / (n_total - k)
    logger.info(f"  KW: H={kw_stat:.4f} p={kw_p:.4f} eta2={kw_eta2:.4f}")

    # ── 10. Section type distribution ─────────────────────────────────────────
    type_counts: dict[str, int] = defaultdict(int)
    for t in gold_types:
        type_counts[t] += 1

    # ── 11. Reliability assessment ────────────────────────────────────────────
    logger.info("Reliability assessment")
    mean_ci_width = np.mean([method_ci[m][2] - method_ci[m][1] for m in METHODS])
    any_sig = any(r["significant_hb_alpha05"] for r in pairwise_comparisons)
    avg_effect = np.mean([abs(r["hedges_g"]) for r in pairwise_comparisons])
    avg_halluc = np.mean([halluc[m]["rate_pct"] for m in METHODS])

    # Reliability criteria:
    # - sample size ≥ 150 → OK
    # - CI width < 0.03 → narrow
    # - internal coherence: TF-ISF leads per summary
    # - LLM: free model (tencent/hy3:free) — uncertain quality
    reliability_notes = []
    reliability_score = "medium"
    if n >= 150:
        reliability_notes.append(f"sample_size={n} (adequate)")
    else:
        reliability_notes.append(f"sample_size={n} (low)")
        reliability_score = "low"
    if mean_ci_width < 0.04:
        reliability_notes.append(f"mean_CI_width={mean_ci_width:.4f} (narrow)")
    else:
        reliability_notes.append(f"mean_CI_width={mean_ci_width:.4f} (wide)")
    if any_sig:
        reliability_notes.append("at_least_one_pair_significant_after_HB")
    else:
        reliability_notes.append("no_pairs_significant_after_HB_correction")
        reliability_score = "low"
    if avg_effect < 0.2:
        reliability_notes.append(f"avg_hedges_g={avg_effect:.3f} (negligible)")
    else:
        reliability_notes.append(f"avg_hedges_g={avg_effect:.3f}")
    reliability_notes.append(f"llm_model={llm_model} (free_tier_uncertain_quality)")
    if avg_halluc > 20:
        reliability_notes.append(f"avg_halluc_rate={avg_halluc:.1f}% (high_LLM_confabulation)")
        reliability_score = "low"
    reliability_note_str = "; ".join(reliability_notes)
    logger.info(f"Reliability: {reliability_score} — {reliability_note_str}")

    # ── 12. Build output ──────────────────────────────────────────────────────
    logger.info("Assembling output")

    # metrics_agg (all numeric top-level metrics)
    metrics_agg = {
        "n_examples": float(n),
        "n_methods": float(len(METHODS)),
        # per-method mean F1
        "cosine_mean_f1": float(f1["cosine"].mean()),
        "bm25_mean_f1": float(f1["bm25"].mean()),
        "tf_isf_mean_f1": float(f1["tf_isf"].mean()),
        # best method mean F1
        "best_method_f1": max(f1[m].mean() for m in METHODS),
        # pairwise diffs
        "tf_isf_vs_cosine_diff": float(f1["tf_isf"].mean() - f1["cosine"].mean()),
        "tf_isf_vs_bm25_diff": float(f1["tf_isf"].mean() - f1["bm25"].mean()),
        "bm25_vs_cosine_diff": float(f1["bm25"].mean() - f1["cosine"].mean()),
        # effect sizes
        "tf_isf_vs_cosine_hedges_g": pairwise_comparisons[0]["hedges_g"],
        "tf_isf_vs_bm25_hedges_g": pairwise_comparisons[1]["hedges_g"],
        "bm25_vs_cosine_hedges_g": pairwise_comparisons[2]["hedges_g"],
        # p values
        "tf_isf_vs_cosine_p_hb": pairwise_comparisons[0]["p_holm_bonferroni"],
        "tf_isf_vs_bm25_p_hb": pairwise_comparisons[1]["p_holm_bonferroni"],
        "bm25_vs_cosine_p_hb": pairwise_comparisons[2]["p_holm_bonferroni"],
        # KW
        "kruskal_wallis_H": float(kw_stat),
        "kruskal_wallis_p": float(kw_p),
        "kruskal_wallis_eta2": float(kw_eta2),
        # hallucination
        "cosine_halluc_rate_pct": float(halluc["cosine"]["rate_pct"]),
        "bm25_halluc_rate_pct": float(halluc["bm25"]["rate_pct"]),
        "tf_isf_halluc_rate_pct": float(halluc["tf_isf"]["rate_pct"]),
        # recall
        "cosine_mean_recall": float(recall["cosine"].mean()),
        "bm25_mean_recall": float(recall["bm25"].mean()),
        "tf_isf_mean_recall": float(recall["tf_isf"].mean()),
        # CI widths
        "cosine_ci_width": float(method_ci["cosine"][2] - method_ci["cosine"][1]),
        "bm25_ci_width": float(method_ci["bm25"][2] - method_ci["bm25"][1]),
        "tf_isf_ci_width": float(method_ci["tf_isf"][2] - method_ci["tf_isf"][1]),
    }

    # per-example records
    per_example = []
    for i in range(n):
        ex_record = {
            "input": gold_answers[i][:200] if len(gold_answers[i]) > 200 else gold_answers[i],  # placeholder: store gold
            "output": gold_answers[i][:500] if len(gold_answers[i]) > 500 else gold_answers[i],
            "metadata_gold_section_type": gold_types[i],
            "predict_cosine": answers["cosine"][i][:300] if len(answers["cosine"][i]) > 300 else answers["cosine"][i],
            "predict_bm25": answers["bm25"][i][:300] if len(answers["bm25"][i]) > 300 else answers["bm25"][i],
            "predict_tf_isf": answers["tf_isf"][i][:300] if len(answers["tf_isf"][i]) > 300 else answers["tf_isf"][i],
            "eval_f1_cosine": float(f1["cosine"][i]),
            "eval_f1_bm25": float(f1["bm25"][i]),
            "eval_f1_tf_isf": float(f1["tf_isf"][i]),
            "eval_recall_cosine": float(recall["cosine"][i]),
            "eval_recall_bm25": float(recall["bm25"][i]),
            "eval_recall_tf_isf": float(recall["tf_isf"][i]),
            "eval_tf_isf_beats_cosine": float(1.0 if f1["tf_isf"][i] > f1["cosine"][i] else 0.0),
            "eval_tf_isf_beats_bm25": float(1.0 if f1["tf_isf"][i] > f1["bm25"][i] else 0.0),
            "eval_halluc_cosine": float(1.0 if (f1["cosine"][i] > 0 and recall["cosine"][i] == 0) else 0.0),
            "eval_halluc_bm25": float(1.0 if (f1["bm25"][i] > 0 and recall["bm25"][i] == 0) else 0.0),
            "eval_halluc_tf_isf": float(1.0 if (f1["tf_isf"][i] > 0 and recall["tf_isf"][i] == 0) else 0.0),
        }
        per_example.append(ex_record)

    output = {
        "metadata": {
            "evaluation_name": "TF-ISF vs BM25 vs Cosine — Comprehensive Evaluation",
            "experiment": "iter_1 (n=180, tencent/hy3:free)",
            "note": (
                "Only one experiment available (iter_1, n=180). "
                "Artifact plan references a second experiment (n=200) which has not been executed yet. "
                "All metrics computed on the single available experiment."
            ),
            "n_bootstrap": N_BOOTSTRAP,
            "random_seed": RNG_SEED,
            "llm_model": llm_model,
            "methods": METHODS,
            "pairwise_comparisons": pairwise_comparisons,
            "method_bootstrap_ci": {
                m: {"mean": method_ci[m][0], "ci_lo": method_ci[m][1], "ci_hi": method_ci[m][2]}
                for m in METHODS
            },
            "descriptive_stats_f1": desc_stats,
            "descriptive_stats_recall": recall_stats,
            "hallucination_rates": halluc,
            "subgroup_by_section_type": subgroup_results,
            "section_type_counts": dict(type_counts),
            "kruskal_wallis": {
                "H_statistic": float(kw_stat),
                "p_value": float(kw_p),
                "eta_squared_approx": float(kw_eta2),
                "interpretation": (
                    "Kruskal-Wallis tests whether F1 distributions differ across methods. "
                    "eta_squared approximates % variance explained by method choice."
                ),
            },
            "reliability_assessment": {
                "score": reliability_score,
                "notes": reliability_notes,
                "recommendation": (
                    "The iter_1 experiment (n=180, free LLM) is the ONLY available result. "
                    "Holm-Bonferroni corrected tests indicate whether TF-ISF improvements are "
                    "statistically significant. Effect sizes (Hedges' g) quantify practical "
                    "significance. High hallucination rates would suggest LLM quality limits "
                    "the signal. Without a second experiment run, the claimed direction "
                    "(TF-ISF > BM25 > Cosine) cannot be confirmed across settings."
                ),
            },
        },
        "metrics_agg": metrics_agg,
        "datasets": [
            {
                "dataset": "QASPER",
                "examples": per_example,
            }
        ],
    }

    out_path = WORKSPACE / "full_eval_out.json"
    out_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")

    # Summary
    logger.info("=" * 60)
    logger.info("RESULTS SUMMARY")
    logger.info(f"  n={n}, LLM={llm_model}")
    for m in METHODS:
        mu, lo, hi = method_ci[m]
        logger.info(f"  {m}: F1={mu:.4f} 95%CI=[{lo:.4f},{hi:.4f}]")
    for r in pairwise_comparisons:
        sig = "SIGNIFICANT" if r["significant_hb_alpha05"] else "not significant"
        logger.info(
            f"  {r['pair']}: diff={r['diff']:+.4f} g={r['hedges_g']:.3f} "
            f"p_hb={r['p_holm_bonferroni']:.4f} [{sig}]"
        )
    logger.info(f"  KW: H={kw_stat:.3f} p={kw_p:.4f} eta2={kw_eta2:.4f}")
    logger.info(f"  Reliability: {reliability_score}")
    logger.info("=" * 60)

    return output


if __name__ == "__main__":
    main()
