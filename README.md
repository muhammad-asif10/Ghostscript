# Ghostscript PDF Compressor

A lightweight, cross-platform utility for batch compressing PDF files using [Ghostscript](https://www.ghostscript.com/). Available as both a Python script (with a progress bar) and a Windows Batch script.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
   - [Python Script](#option-a-python-script)
   - [Windows Batch Script](#option-b-windows-batch-script)
7. [PDF Quality Settings](#pdf-quality-settings)
8. [Project Structure](#project-structure)
9. [Troubleshooting](#troubleshooting)

---

## Overview

Ghostscript PDF Compressor lets you shrink the file size of one or many PDF documents in a single command. It wraps the Ghostscript command-line tool with a friendly Python or Batch interface, automatically scans an input folder, compresses every PDF it finds, and saves the results to a separate output folder — all without overwriting your originals.

---

## Features

- **Batch processing** — compress every PDF in a folder in one run
- **Progress tracking** — real-time progress bar in the Python version (`tqdm`)
- **Non-destructive** — originals are never modified; output goes to a dedicated folder
- **Configurable quality** — choose from four Ghostscript quality presets
- **Two interfaces** — Python script for all platforms; Batch script for quick Windows use
- **Auto-creates output folder** — no manual setup required before each run

---

## Prerequisites

### 1. Ghostscript

Download and install Ghostscript for your operating system:

| Platform | Download |
|----------|----------|
| Windows  | [ghostscript.com/download/gsdnld.html](https://www.ghostscript.com/download/gsdnld.html) |
| macOS    | `brew install ghostscript` |
| Linux    | `sudo apt install ghostscript` |

> **Note:** The scripts default to the Windows 64-bit executable path `C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe`. See [Configuration](#configuration) if your installation path differs.

### 2. Python 3 *(for the Python script only)*

- Python 3.6 or later — [python.org/downloads](https://www.python.org/downloads/)
- `pip` (bundled with Python 3.4+)

### 3. tqdm *(for the Python script only)*

`tqdm` provides the progress bar. Install it with:

```bash
pip install tqdm
```

---

## Installation

1. **Clone or download this repository:**

   ```bash
   git clone https://github.com/muhammad-asif10/Ghostscript.git
   cd Ghostscript
   ```

2. **Install the Python dependency:**

   ```bash
   pip install tqdm
   ```

3. **Create the input folder and add your PDFs:**

   ```
   Ghostscript/
   └── pdf/           ← place your PDF files here
   ```

That is all the setup required. The output folder (`compressed_file/`) is created automatically on first run.

---

## Configuration

Both scripts contain a small set of variables at the top that you can edit to match your environment.

### Python script — `compress_pdfs.py`

| Variable | Default | Description |
|----------|---------|-------------|
| `GS_PATH` | `C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe` | Full path to the Ghostscript executable |
| `INPUT_FOLDER` | `pdf` | Folder that contains the PDFs to compress |
| `OUTPUT_FOLDER` | `compressed_file` | Folder where compressed PDFs are saved |

**Example — Linux/macOS path:**

```python
GS_PATH = "/usr/bin/gs"
```

**Example — custom folders:**

```python
INPUT_FOLDER  = "originals"
OUTPUT_FOLDER = "smaller"
```

### Batch script — `Compressor.bat`

| Variable | Default | Description |
|----------|---------|-------------|
| `GS_OUTPUT_DIR` | `compressed_files` | Folder where compressed PDFs are saved |
| Ghostscript path (line 16) | `C:\Program Files\gs\gs10.06.0\bin\gswin64c.exe` | Full path to the Ghostscript executable |

> The Batch script processes PDFs located **in the same directory** as `Compressor.bat`.

---

## Usage

### Option A: Python Script

1. Place your PDF files in the `pdf/` folder.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python compress_pdfs.py
   ```

4. Monitor the progress bar:

   ```
   Found 5 PDFs. Compressing...

   Compressing PDFs: 100%|██████████| 5/5 [00:12<00:00, 2.4s/file]

   All PDFs compressed successfully.
   ```

5. Retrieve the compressed files from the `compressed_file/` folder.

---

### Option B: Windows Batch Script

1. Copy (or move) your PDF files into the same folder as `Compressor.bat`.
2. Double-click `Compressor.bat`, or run it from a Command Prompt:

   ```cmd
   Compressor.bat
   ```

3. Watch the per-file progress:

   ```
   [1/5] Compressing report.pdf
   [2/5] Compressing invoice.pdf
   ...
   DONE. All 5 files compressed.
   ```

4. Retrieve the compressed files from the `compressed_files\` sub-folder.

---

## PDF Quality Settings

Both scripts use the `-dPDFSETTINGS` flag to control the trade-off between file size and output quality. The default is `/screen`. Change it to match your use case:

| Setting | Resolution | Best For | Relative File Size |
|---------|-----------|----------|--------------------|
| `/screen` | 72 dpi | Web / email sharing | Smallest |
| `/ebook` | 150 dpi | E-readers / tablets | Small |
| `/printer` | 300 dpi | Desktop printing | Medium |
| `/prepress` | 300 dpi (colour-managed) | Professional printing / archiving | Largest |

### Changing the quality preset

**Python script** (`compress_pdfs.py`, line 28):

```python
# Change /screen to your preferred preset
"-dPDFSETTINGS=/ebook",
```

**Batch script** (`Compressor.bat`, line 16):

```bat
... -dPDFSETTINGS=/ebook ...
```

---

## Project Structure

```
Ghostscript/
├── compress_pdfs.py   # Python batch-compression script
├── Compressor.bat     # Windows batch-compression script
├── pdf/               # (create this) place input PDFs here
└── compressed_file/   # (auto-created) output destination
```

---

## Troubleshooting

### "No PDF files found."
Make sure your PDF files are placed inside the `pdf/` folder (Python) or the same directory as `Compressor.bat` (Batch) before running.

### Ghostscript not found / subprocess error
Verify the Ghostscript executable path in the script matches your installation:

```bash
# Windows — find the installed path
where gswin64c

# macOS / Linux
which gs
```

Then update `GS_PATH` (Python) or the path on line 16 (Batch) accordingly.

### Output PDFs are empty or corrupted
- Confirm the Ghostscript version supports the source PDF.
- Try a less aggressive quality preset (e.g., `/ebook` or `/printer`).
- Remove the `-dQUIET` flag temporarily to see Ghostscript's full output.

### `ModuleNotFoundError: No module named 'tqdm'`
Install the missing dependency:

```bash
pip install tqdm
```
