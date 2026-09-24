"""Create a byte-for-byte reproducible LegacyLens input archive."""
import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "samples" / "facturaya-v1"
ALLOWED = {".py", ".sql", ".txt", ".md", ".html"}


def package(destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    paths = sorted(path for path in SAMPLE.rglob("*") if path.is_file() and path.suffix in ALLOWED
                   and not any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(SAMPLE).parts))
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in paths:
            info = zipfile.ZipInfo("facturaya-v1/" + path.relative_to(SAMPLE).as_posix())
            info.date_time = (2024, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output", nargs="?", default=str(ROOT / "dist" / "facturaya-v1.zip"))
    args = parser.parse_args()
    print(f"Packaged {len(package(args.output))} files: {args.output}")
