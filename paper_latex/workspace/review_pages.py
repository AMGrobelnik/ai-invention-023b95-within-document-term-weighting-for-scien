import fitz  # pymupdf
import os

pdf_path = "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.pdf"
out_dir = "/ai-inventor/aii_data/runs/run_gjLlrqQuoUxT/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pages"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=120)
    out_path = f"{out_dir}/page_{i+1:02d}.png"
    pix.save(out_path)
    print(f"Saved {out_path}")
print("Done.")
