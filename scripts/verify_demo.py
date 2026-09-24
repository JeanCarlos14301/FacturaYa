"""Verify the evaluation snapshot and exact source evidence."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", ".venv", ".pytest_cache", "__pycache__", "evaluation", "dist"}
EXCLUDED_SUFFIXES = {".db", ".sqlite3", ".pyc", ".zip", ".tmp"}


def source_paths():
    return sorted(
        path for path in ROOT.rglob("*") if path.is_file()
        and not any(part in EXCLUDED_DIRS or part.startswith(".") and part != ".gitignore"
                    for part in path.relative_to(ROOT).parts)
        and path.suffix not in EXCLUDED_SUFFIXES
    )


def snapshot_sha256():
    digest = hashlib.sha256()
    for path in source_paths():
        relative = path.relative_to(ROOT).as_posix()
        file_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        digest.update(relative.encode("utf-8") + b"\0" + file_hash.encode("ascii") + b"\n")
    return digest.hexdigest()


def verify(manifest):
    assert manifest["snapshot_sha256"] == snapshot_sha256(), "Snapshot hash changed"
    for finding in manifest["findings"]:
        for evidence in finding["evidence"]:
            path = ROOT / evidence["path"]
            lines = path.read_text(encoding="utf-8").splitlines()
            first, last = evidence["line_start"], evidence["line_end"]
            assert 1 <= first <= last <= len(lines), (finding["id"], path)
            assert evidence["fragment"] in "\n".join(lines[first - 1:last]), (finding["id"], path)
    return len(manifest["findings"])


if __name__ == "__main__":
    manifest = json.loads((ROOT / "evaluation" / "expected-findings.json").read_text(encoding="utf-8"))
    print(f"Verified {verify(manifest)} findings; snapshot {manifest['snapshot_sha256']}")
