"""WebSe_RadioList -- Selenium-Implementierung fuer Radio-Button-Gruppen.

YAML-Beispiel::

    MyRadios:
      class: okw_web_selenium.widgets.webse_radiolist.WebSe_RadioList
      locator: { css: '[name="paymentMethod"]' }
      group: paymentMethod          # optional, falls Locator keine name= enthält
"""

import re as _re
from .webse_base import WebSe_Base


class WebSe_RadioList(WebSe_Base):

    def __init__(self, adapter, locator, **options):
        super().__init__(adapter, locator, **options)
        self.group = options.get('group')

    # ------------------------------------------------------------------
    # Helfer
    # ------------------------------------------------------------------
    def _extract_name_from_locator(self):
        loc = self.locator
        if isinstance(loc, dict) and len(loc) == 1:
            key, sel = list(loc.items())[0]
            if key == 'css' and sel and 'name=' in sel:
                m = _re.search(r'name\s*=\s*"([^"]+)"', sel)
                if m:
                    return m.group(1)
        if isinstance(loc, str) and loc.startswith('css:') and 'name=' in loc:
            m = _re.search(r'name\s*=\s*"([^"]+)"', loc)
            if m:
                return m.group(1)
        return None

    def _container_css(self):
        loc = self.locator
        if isinstance(loc, dict) and len(loc) == 1:
            key, sel = list(loc.items())[0]
            if key == 'css':
                return sel
        if isinstance(loc, str) and loc.startswith('css:'):
            return loc.split(':', 1)[1]
        return None

    def _current_value(self):
        name_from_loc = self._extract_name_from_locator()
        if name_from_loc:
            css = f"css:input[type='radio'][name='{name_from_loc}']:checked"
            return self.adapter.get_attribute(css, 'value')
        container = self._container_css()
        if container:
            checked = f"css:{container} input[type='radio']:checked"
            return self.adapter.get_attribute(checked, 'value')
        if self.group:
            css = f"css:input[type='radio'][name='{self.group}']:checked"
            return self.adapter.get_attribute(css, 'value')
        return None

    def _resolve_group_name(self):
        return self._extract_name_from_locator() or self.group

    # ------------------------------------------------------------------
    # OkwWidget-Methoden
    # ------------------------------------------------------------------
    def okw_select(self, value: str):
        self._wait_before('write')
        name_from_loc = self._extract_name_from_locator()
        if name_from_loc:
            self.adapter.select_radio(name_from_loc, value)
            return
        container = self._container_css()
        if container:
            combined = f"css:{container} input[type='radio'][value='{value}']"
            self.adapter.click(combined)
            return
        if not self.group:
            raise ValueError(
                "WebSe_RadioList needs either 'group' or a locator with [name=...] or a container locator")
        self.adapter.select_radio(self.group, value)

    def okw_get_value(self) -> str:
        val = self._current_value()
        return val if val is not None else ""

    def okw_get_list_count(self) -> int:
        name_from_loc = self._extract_name_from_locator()
        if name_from_loc:
            css = f"css:input[type='radio'][name='{name_from_loc}']"
            return len(self.sl.get_webelements(self.adapter._resolve(css)))
        container = self._container_css()
        if container:
            css = f"css:{container} input[type='radio']"
            return len(self.sl.get_webelements(self.adapter._resolve(css)))
        if self.group:
            css = f"css:input[type='radio'][name='{self.group}']"
            return len(self.sl.get_webelements(self.adapter._resolve(css)))
        raise ValueError("WebSe_RadioList needs group or locator with [name=...]")

    def okw_get_selected_count(self) -> int:
        name_from_loc = self._extract_name_from_locator()
        if name_from_loc:
            css = f"css:input[type='radio'][name='{name_from_loc}']:checked"
            return len(self.sl.get_webelements(self.adapter._resolve(css)))
        container = self._container_css()
        if container:
            css = f"css:{container} input[type='radio']:checked"
            return len(self.sl.get_webelements(self.adapter._resolve(css)))
        if self.group:
            css = f"css:input[type='radio'][name='{self.group}']:checked"
            return len(self.sl.get_webelements(self.adapter._resolve(css)))
        raise ValueError("WebSe_RadioList needs group or locator with [name=...]")
