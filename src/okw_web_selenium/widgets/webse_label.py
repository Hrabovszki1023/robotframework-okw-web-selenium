"""WebSe_Label -- Selenium-Implementierung fuer Labels / statischen Text."""

from .webse_base import WebSe_Base


class WebSe_Label(WebSe_Base):
    """Read-only Label-Widget. Wert = sichtbarer Text."""

    def okw_get_value(self) -> str:
        return self.adapter.get_text(self.locator) or ""
