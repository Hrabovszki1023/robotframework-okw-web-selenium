"""WebSe_TextField -- Selenium-Implementierung fuer Textfelder (input, textarea)."""

from .webse_base import WebSe_Base


class WebSe_TextField(WebSe_Base):

    def okw_type_key(self, key: str):
        self._wait_before('write')
        self.adapter.press_keys(self.locator, key)

    def okw_set_value(self, value: str):
        self._wait_before('write')
        try:
            self.adapter.clear_text(self.locator)
        except Exception:
            pass
        self.adapter.input_text(self.locator, value)

    def okw_get_value(self) -> str:
        return self.adapter.get_value(self.locator) or ""
