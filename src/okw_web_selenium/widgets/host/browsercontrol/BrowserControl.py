from okw4robot.widgets.okw_widget import OkwWidget


class BrowserControl(OkwWidget):

    def __init__(self, adapter, locator):
        self.adapter = adapter
        self.locator = locator  # virtual; not used

    def okw_click(self):
        self.adapter.maximize_window()
