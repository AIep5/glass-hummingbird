"""Place the entry image at /output/entry.png.

The program does one thing: it reads the image that sits next to
this file and writes those exact bytes out again. It talks to no
network, rolls no dice, and never looks at the clock, so running it
twice produces the same file twice, byte for byte.
"""

from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")


def run() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing entry image: {SOURCE}")
    picture = SOURCE.read_bytes()
    if not picture:
        raise SystemExit("entry image is empty, refusing to write it out")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(picture)
    print(f"wrote {TARGET} ({len(picture)} bytes)")


if __name__ == "__main__":
    run()
