from okw4robot.widgets.base.base_widget import BaseWidget

class BrowserControl(BaseWidget):
    # def __init__(self, adapter, locator):
    #     self.adapter = adapter
    #    self.locator = locator  # virtual; not used
    def __init__(self, adapter, locator):
        self.adapter = adapter
        self.locator = locator  # virtual; not used

    def okw_click(self):
        self.adapter.maximize_window()
