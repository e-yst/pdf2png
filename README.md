# pdf2png

This Python script converts PDF files into individual image files (PNG format). It utilizes the `magika` library for PDF identification and the `pdf2image` library for conversion.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- `magika` library
- `pdf2image` library

## Usage

1. Clone this repository or download the script directly.
2. Install the required dependencies:

    ```bash
    pip install magika pdf2image
    ```

3. Run the script with the path to your PDF file as an argument:

    ```bash
    python pdf_to_image.py path/to/your/file.pdf
    ```

4. The script will create individual PNG images from each page of the PDF. The output files will be named as follows:

    - For a single-page PDF: `file_001.png`
    - For multi-page PDFs: `file_001.png`, `file_002.png`, ..., `file_NNN.png`

## Example

Suppose you have a PDF file named `my_document.pdf`. Running the script:

```bash
python pdf_to_image.py my_document.pdf
```

will generate PNG files in the same directory as the PDF.
