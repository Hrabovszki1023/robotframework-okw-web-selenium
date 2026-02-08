from ..base.base_widget import BaseWidget


class CheckBox(BaseWidget):
    def okw_click(self):
        # Toggles checkbox
        self._wait_before('write')
        self.adapter.click(self.locator)

    def okw_set_value(self, value):
        self._wait_before('write')
        norm = str(value).strip().lower()
        if norm in ("true", "checked", "yes", "1"):
            target = True
        elif norm in ("false", "unchecked", "no", "0"):
            target = False
        else:
            raise ValueError(f"Unsupported checkbox value: {value}")
        self.adapter.set_checkbox(self.locator, target)

    def okw_verify_value(self, expected):
        norm = str(expected).strip().lower()
        if norm not in ("checked", "unchecked"):
            raise ValueError("Checkbox expected must be 'Checked' or 'Unchecked'")
        is_sel = self.adapter.is_checkbox_selected(self.locator)
        if norm == "checked" and not is_sel:
            raise AssertionError("[CheckBox] Expected Checked, but was Unchecked")
        if norm == "unchecked" and is_sel:
            raise AssertionError("[CheckBox] Expected Unchecked, but was Checked")

    def okw_log_value(self):
        print("LOG:", "Checked" if self.adapter.is_checkbox_selected(self.locator) else "Unchecked")

    def okw_memorize_value(self):
        return "Checked" if self.adapter.is_checkbox_selected(self.locator) else "Unchecked"
