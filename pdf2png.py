import sys
from argparse import ArgumentParser
from pathlib import Path

from magika import Magika
from pdf2image import convert_from_path


def build_parser():
    parser = ArgumentParser()
    parser.add_argument("pdf_path")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        sys.exit(f"{pdf_path} not exists.")

    m = Magika()
    res = m.identify_path(pdf_path)
    if res.output.ct_label != "pdf":
        sys.exit(f"{pdf_path} is not a pdf file.")

    images = convert_from_path(args.pdf_path)
    for idx, img in enumerate(images, start=1):
        output_path = Path(f"{pdf_path.stem}_{str(idx).zfill(3)}.png")
        img.save(output_path)

    print(f"Output directory: {output_path.parent.absolute()}")
    output_file_str = (
        f"{pdf_path.stem}_001.png"
        if len(images) == 1
        else f"{pdf_path.stem}_001.png ... "
        f"{pdf_path.stem}_{str(len(images)).zfill(3)}.png"
    )
    print(f"Output file{'s' if len(images)>1 else ''}: {output_file_str}")


if __name__ == "__main__":
    main()
