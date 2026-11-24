"""A single joke about cats, one line under 200 characters.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "My cat walked across my keyboard once and typed a stronger password than I have ever chosen, then sat on the laptop and demanded I thank her for the security audit."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
