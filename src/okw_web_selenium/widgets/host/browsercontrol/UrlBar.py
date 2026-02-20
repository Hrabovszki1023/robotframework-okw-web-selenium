from okw4robot.widgets.okw_widget import OkwWidget


class UrlBar(OkwWidget):

    def __init__(self, adapter, locator, **options):
        super().__init__(adapter, locator, **options)

    def okw_set_value(self, value):
        self.log_current_method(f"Navigating to: {value}")
        self.adapter.go_to(value)
