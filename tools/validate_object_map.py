from pathlib import Path
import sys, yaml

REQ = ("class", "locator")

def validate_file(path: Path) -> int:
    ok = True
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    for section, entries in data.items():
        if not isinstance(entries, dict):
            print(f"[ERROR] {path}: Section '{section}' ist keine Map", file=sys.stderr)
            ok = False
            continue
        for name, cfg in entries.items():
            if not isinstance(cfg, dict):
                print(f"[ERROR] {path}: Eintrag '{name}' ist keine Map", file=sys.stderr)
                ok = False
                continue
            missing = [k for k in REQ if k not in cfg and name != "__self__"]
            if missing:
                print(f"[ERROR] {path}: '{section}.{name}' fehlt {missing}", file=sys.stderr)
                ok = False
    return 0 if ok else 2

def main():
    base = Path("locators")
    rc = 0
    for f in base.rglob("*.objects.yaml"):
        rc |= validate_file(f)
    sys.exit(rc)

if __name__ == "__main__":
    main()
