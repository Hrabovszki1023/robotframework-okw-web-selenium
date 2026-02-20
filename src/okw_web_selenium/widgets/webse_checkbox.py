"""WebSe_CheckBox -- Selenium-Implementierung fuer Checkboxen."""

from .webse_base import WebSe_Base


class WebSe_CheckBox(WebSe_Base):

    def okw_set_value(self, value: str):
        self._wait_before('write')
        norm = str(value).strip().lower()
        if norm in ("true", "checked", "yes", "1"):
            target = True
        elif norm in ("false", "unchecked", "no", "0"):
            target = False
        else:
            raise ValueError(f"Unsupported checkbox value: {value}")
        self.adapter.set_checkbox(self.locator, target)

    def okw_get_value(self) -> str:
        return "Checked" if self.adapter.is_checkbox_selected(self.locator) else "Unchecked"
