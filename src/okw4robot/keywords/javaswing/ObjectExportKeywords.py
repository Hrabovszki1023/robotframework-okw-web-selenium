# src/okw4robot/keywords/object_expjavaswing/ObjectExportKeywords.py

from robot.api.deco import keyword
from pathlib import Path
import yaml
from ...runtime.context import context

class ObjectExportKeywords:

    @keyword("Export Object Tree To File")
    def exportiere_objektstruktur(self, pfad="objecttree.yaml"):
        """
        Exportiert die aktuelle GUI-Objektstruktur des aktiven Adapters
        in eine YAML-Datei.
        """
        adapter = context.get_adapter()
        tree = adapter.get_object_tree()

        path = Path(pfad).resolve()
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(tree, f, allow_unicode=True)

        print(f"[Exportiere Objektstruktur] Objektbaum gespeichert unter: {path}")
