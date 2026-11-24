"""Write a two-line explanation of an everyday thing for a 10-year-old.

Line 1 explains a traffic jam through one concrete analogy (a zipper
stuck halfway). Line 2 says honestly what the analogy maps and what it
leaves out. Output: /output/entry.txt, exactly two lines, 1-400 chars.
"""

import os

LINE_1 = (
    "A traffic jam is a zipper stuck halfway: each car is a tooth waiting "
    "its turn to slide through, and one tooth shoving out of line snags the "
    "whole jacket."
)
LINE_2 = (
    "The zipper maps how cars must pass one at a time in order, but it "
    "leaves out that drivers can choose another road, and that unlike a "
    "zipper they get bored, tired, and angry."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
