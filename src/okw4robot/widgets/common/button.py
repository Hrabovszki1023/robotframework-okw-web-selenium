from ..base.base_widget import BaseWidget

class Button(BaseWidget):
    def okw_click(self):
        # Sync before clicking
        self._wait_before('write')
        self.adapter.click(self.locator)

    def okw_double_click(self):
        self._wait_before('write')
        self.adapter.double_click(self.locator)
