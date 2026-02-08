from ..base.base_widget import BaseWidget

class Label(BaseWidget):
    def okw_verify_value(self, expected):
        actual = self.adapter.get_text(self.locator)
        if actual != expected:
            raise AssertionError(f"Expected '{expected}', got '{actual}'")

    def okw_log_value(self):
        print("LOG:", self.adapter.get_text(self.locator))

    def okw_memorize_value(self):
        return self.adapter.get_text(self.locator)

    def okw_verify_value_wcm(self, expected):
        import re
        value = self.adapter.get_text(self.locator)
        pattern = '^' + re.escape(expected).replace(r'\*', '.*').replace(r'\?', '.') + '$'
        if not re.compile(pattern, re.DOTALL).match(value):
            raise AssertionError(f"[VerifyValueWCM] Value '{value}' does not match pattern '{expected}'")

    def okw_verify_value_regex(self, expected):
        import re
        value = self.adapter.get_text(self.locator)
        if not re.search(expected, value):
            raise AssertionError(f"[VerifyValueREGX] Value '{value}' does not match regex '{expected}'")
