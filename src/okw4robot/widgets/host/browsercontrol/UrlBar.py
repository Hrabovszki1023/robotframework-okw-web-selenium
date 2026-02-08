from okw4robot.widgets.base.base_widget import BaseWidget

class UrlBar(BaseWidget):
    # def __init__(self, adapter, locator):
    #     self.adapter = adapter
    #    self.locator = locator  # virtual; not used

    def okw_set_value(self, value):
        self.log_current_method(f"Navigating to: {value}")
        self.adapter.go_to(value)
