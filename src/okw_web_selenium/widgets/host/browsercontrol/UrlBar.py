from okw4robot.widgets.okw_widget import OkwWidget


class UrlBar(OkwWidget):

    def okw_set_value(self, value):
        self.log_current_method(f"Navigating to: {value}")
        self.adapter.go_to(value)
