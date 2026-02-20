from okw4robot.widgets.okw_widget import OkwWidget


class BrowserControl(OkwWidget):

    def __init__(self, adapter, locator, **options):
        super().__init__(adapter, locator, **options)

    def okw_click(self):
        self.adapter.maximize_window()
