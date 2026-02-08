from pathlib import Path
import yaml
from importlib.resources import files

def load_yaml_with_fallback(name: str) -> dict:
    """
    Lädt eine YAML-Datei aus dem Projektverzeichnis oder fällt auf das Framework zurück.
    `name` ist ein relativer Pfad ohne ".yaml" – z. B. "web/TestAppOKW4Robot_WEB"
    """
    # 1. Projektverzeichnis: ./locators/web/Datei.yaml
    local_path = Path("locators") / f"{name}.yaml"
    if local_path.exists():
        with open(local_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    # 2. Framework-Verzeichnis: src/okw4robot/locators/web/Datei.yaml
    parts = name.split("/")
    if len(parts) == 1:
        res_path = files("okw4robot.locators").joinpath(f"{parts[0]}.yaml")
    else:
        subpkg = ".".join(["okw4robot", "locators"] + parts[:-1])
        res_path = files(subpkg).joinpath(f"{parts[-1]}.yaml")

    if not res_path.exists():
        raise FileNotFoundError(f"App YAML not found: {name}.yaml")

    with open(res_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
