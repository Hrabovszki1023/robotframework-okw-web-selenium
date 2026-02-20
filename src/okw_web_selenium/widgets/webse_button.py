"""WebSe_Button -- Selenium-Implementierung fuer Buttons."""

from .webse_base import WebSe_Base


class WebSe_Button(WebSe_Base):
    """Button-Widget. Click und DoubleClick aus WebSe_Base genuegen."""

    def okw_get_value(self) -> str:
        """Fuer Buttons: sichtbarer Text als 'Value'."""
        return self.adapter.get_text(self.locator) or ""
