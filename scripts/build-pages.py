#!/usr/bin/env python3
"""Build the static site, preserving root-level URLs for all papers/*.pdf files."""

from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def build(destination: Path) -> None:
    # Require a fresh directory to avoid publishing stale or removed files.
    destination.mkdir(parents=True, exist_ok=False)
    for name in ("index.html", "CNAME", ".nojekyll"):
        shutil.copy2(ROOT / name, destination / name)
    for name in ("media", "papers"):
        shutil.copytree(ROOT / name, destination / name)
    for paper in (ROOT / "papers").glob("*.pdf"):
        shutil.copy2(paper, destination / paper.name)


if __name__ == "__main__":
    build(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site")
