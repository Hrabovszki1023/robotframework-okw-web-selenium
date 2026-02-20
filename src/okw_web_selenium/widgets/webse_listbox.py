"""WebSe_ListBox -- Selenium-Implementierung fuer Listen (<select multiple>).

SetValue: akzeptiert ein einzelnes Label oder komma-separierte Labels.
"""

from .webse_base import WebSe_Base


class WebSe_ListBox(WebSe_Base):

    def _to_list(self, value):
        if isinstance(value, (list, tuple)):
            return [str(v).strip() for v in value]
        return [v.strip() for v in str(value).split(',') if v.strip()]

    def okw_select(self, value: str):
        self._wait_before('write')
        labels = self._to_list(value)
        if not labels:
            self.adapter.unselect_all_from_list(self.locator)
            return
        self.adapter.select_by_label(self.locator, labels)

    def okw_set_value(self, value: str):
        """Alias fuer okw_select bei ListBox."""
        self.okw_select(value)

    def okw_get_value(self) -> str:
        labels = self.adapter.get_selected_list_labels(self.locator) or []
        return ", ".join(labels)

    def okw_get_list_count(self) -> int:
        el = self.sl.get_webelement(self.adapter._resolve(self.locator))
        return len(el.find_elements("css selector", "option"))

    def okw_get_selected_count(self) -> int:
        vals = self.adapter.get_selected_list_values(self.locator) or []
        return len(vals)
