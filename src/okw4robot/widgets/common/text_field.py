from ..base.base_widget import BaseWidget

class TextField(BaseWidget):
    def okw_type_key(self, key):
        # Send keys to the input element
        self._wait_before('write')
        self.adapter.press_keys(self.locator, key)

    def okw_set_value(self, value):
        self._wait_before('write')
        # Prefer clear+type for stability
        try:
            self.adapter.clear_text(self.locator)
        except Exception:
            pass
        self.adapter.input_text(self.locator, value)

    def okw_click(self):
        self._wait_before('write')
        self.adapter.click(self.locator)

    def okw_verify_value(self, expected):
        actual = self.adapter.get_value(self.locator)
        if actual != expected:
            raise AssertionError(f"Expected '{expected}', got '{actual}'")

    def okw_log_value(self):
        print("LOG:", self.adapter.get_value(self.locator))

    def okw_memorize_value(self):
        return self.adapter.get_value(self.locator)

    def okw_verify_value_wcm(self, expected):
        # WCM = Wildcard Match: * wildcard, ? single char
        import re
        value = self.adapter.get_value(self.locator)
        # Escape regex, then replace wildcards
        pattern = '^' + re.escape(expected).replace(r'\*', '.*').replace(r'\?', '.') + '$'
        if not re.compile(pattern, re.DOTALL).match(value):
            raise AssertionError(f"[VerifyValueWCM] Value '{value}' does not match pattern '{expected}'")

    def okw_verify_value_regex(self, expected):
        import re
        value = self.adapter.get_value(self.locator)
        if not re.search(expected, value):
            raise AssertionError(f"[VerifyValueREGX] Value '{value}' does not match regex '{expected}'")
    
    def okw_exists(self):
        return self.adapter.element_exists(self.locator)

    # Placeholder support
    def _get_placeholder(self):
        ph = None
        try:
            ph = self.adapter.get_attribute(self.locator, 'placeholder')
        except Exception:
            ph = None
        return ph if ph is not None else ""

    def okw_verify_placeholder(self, expected):
        actual = self._get_placeholder()
        if actual != expected:
            raise AssertionError("[VerifyPlaceholder] Expected '" + str(expected) + "', got '" + str(actual) + "'")

    def okw_verify_placeholder_wcm(self, expected):
        import re
        value = self._get_placeholder()
        pattern = '^' + re.escape(expected).replace(r'\*', '.*').replace(r'\?', '.') + '$'
        if not re.compile(pattern, re.DOTALL).match(value):
            raise AssertionError("[VerifyPlaceholderWCM] Value '" + str(value) + "' does not match pattern '" + str(expected) + "'")

    def okw_verify_placeholder_regex(self, expected):
        import re
        value = self._get_placeholder()
        if not re.search(expected, value or ""):
            raise AssertionError("[VerifyPlaceholderREGX] Value '" + str(value) + "' does not match regex '" + str(expected) + "'")

