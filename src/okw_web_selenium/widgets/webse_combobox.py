"""WebSe_ComboBox -- Selenium-Implementierung fuer ComboBoxen.

Unterstuetzt sowohl native <select>-Elemente als auch editierbare
Combo-Inputs mit Dropdown.
"""

from .webse_base import WebSe_Base


class WebSe_ComboBox(WebSe_Base):

    def _is_editable(self) -> bool:
        """Prueft ob die ComboBox editierbar ist (YAML-Override oder Adapter)."""
        if 'editable' in self.options:
            try:
                return bool(self.options.get('editable'))
            except Exception:
                pass
        try:
            if hasattr(self.adapter, 'is_editable'):
                return bool(self.adapter.is_editable(self.locator))
        except Exception:
            pass
        return False

    def okw_select(self, value: str):
        self._wait_before('write')
        self.adapter.select_by_label(self.locator, value)

    def okw_set_value(self, value: str):
        self._wait_before('write')
        editable = self._is_editable()

        if not editable:
            # Nicht editierbar -> Auswahl aus Liste
            try:
                self.adapter.select_by_label(self.locator, value)
                return
            except Exception as e:
                raise AssertionError(
                    f"[WebSe_ComboBox] Non-editable. Value '{value}' not found: {e}")

        # Editierbar -> Tippen + Enter
        try:
            self.adapter.clear_text(self.locator)
        except Exception:
            pass
        self.adapter.input_text(self.locator, value)
        try:
            self.adapter.press_keys(self.locator, "ENTER")
        except Exception:
            pass
        # Fallback: pruefen ob Wert angenommen wurde
        try:
            actual = self.adapter.get_value(self.locator)
            if actual != value:
                self.adapter.select_by_label(self.locator, value)
        except Exception:
            pass

    def okw_type_key(self, key: str):
        try:
            self.adapter.press_keys(self.locator, key)
        except Exception:
            self.adapter.press_keys(None, key)

    def okw_get_value(self) -> str:
        # Input-Value bevorzugen, Fallback auf selektiertes Label
        try:
            val = self.adapter.get_value(self.locator)
            if val:
                return val
        except Exception:
            pass
        try:
            labels = self.adapter.get_selected_list_labels(self.locator)
            if labels:
                return labels[0]
        except Exception:
            pass
        return ""

    # Listen-Unterstuetzung fuer native <select>
    def okw_get_list_count(self) -> int:
        el = self.sl.get_webelement(self.adapter._resolve(self.locator))
        tag = (el.tag_name or '').lower()
        if tag == 'select':
            return len(el.find_elements("css selector", "option"))
        raise NotImplementedError(
            "[WebSe_ComboBox] List count not supported for non-native select.")

    def okw_get_selected_count(self) -> int:
        try:
            labels = self.adapter.get_selected_list_labels(self.locator) or []
            if labels:
                return len(labels)
        except Exception:
            pass
        try:
            val = self.adapter.get_value(self.locator) or ""
            return 1 if str(val) != "" else 0
        except Exception:
            return 0
