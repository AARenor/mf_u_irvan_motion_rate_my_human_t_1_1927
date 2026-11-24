"""Write the make.fun one-line review entry to entry.txt.

Standard library only, no network. Python 3.13 compatible.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Five stars. He asked me to summarize his day. I wrote: argued with a "
    "toaster, lost. He said add nuance. I wrote: twice."
)


def output_dir() -> Path:
    """Folder to write into: MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
