"""Image Pad Square — Pad images to a square canvas with a color or blur fill so a shop listing stays centered."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='image_pad_square',
        description='Pad images to a square canvas with a color or blur fill so a shop listing stays centered.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Image Pad Square')
    print('Square thumbs without cropping the subject.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
