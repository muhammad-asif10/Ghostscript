import os
import subprocess
from tqdm import tqdm

# CHANGE THIS PATH IF YOUR GS PATH IS DIFFERENT
GS_PATH = r"C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe"

INPUT_FOLDER = "pdf"
OUTPUT_FOLDER = "compressed_file"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("No PDF files found.")
    exit()

print(f"Found {len(pdf_files)} PDFs. Compressing...\n")

for pdf in tqdm(pdf_files, desc="Compressing PDFs", unit="file"):
    input_path = os.path.join(INPUT_FOLDER, pdf)
    output_path = os.path.join(OUTPUT_FOLDER, pdf)

    cmd = [
        GS_PATH,
        "-sDEVICE=pdfwrite",
        "-dPDFSETTINGS=/screen",  # /ebook for better quality
        "-dNOPAUSE",
        "-dBATCH",
        "-dQUIET",
        f"-sOutputFile={output_path}",
        input_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("\nAll PDFs compressed successfully.")