from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn

class SeleniumWebAdapter:

    def __init__(self, browser):
        self.browser = browser
        self.sl = SeleniumLibrary()
        self.sl.open_browser("about:blank", browser=self.browser)


    def go_to(self, url):
        self.sl.go_to(url)

    def maximize_window(self):
        self.sl.maximize_browser_window()

    def input_text(self, locator, value):
        resolved = self._resolve(locator)
        self.sl.input_text(resolved, value)

    def click(self, locator):
        resolved = self._resolve(locator)
        self.sl.click_element(resolved)

    def double_click(self, locator):
        resolved = self._resolve(locator)
        # SeleniumLibrary supports double click on element
        self.sl.double_click_element(resolved)

    def get_text(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_text(resolved)

    def get_value(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_value(resolved)

    def get_attribute(self, locator, name):
        resolved = self._resolve(locator)
        # Use WebElement for reliable attribute access
        el = self.sl.get_webelement(resolved)
        return el.get_attribute(name)

    def clear_text(self, locator):
        resolved = self._resolve(locator)
        self.sl.clear_element_text(resolved)

    def element_exists(self, locator):
        try:
            self.sl.get_webelement(self._resolve(locator))
            return True
        except Exception:
            return False

    # Select/Combo support
    def select_by_label(self, locator, label):
        resolved = self._resolve(locator)
        self.sl.select_from_list_by_label(resolved, label)

    def select_by_value(self, locator, value):
        resolved = self._resolve(locator)
        self.sl.select_from_list_by_value(resolved, value)

    def select_by_index(self, locator, index):
        resolved = self._resolve(locator)
        self.sl.select_from_list_by_index(resolved, str(index))

    # Keyboard
    def press_keys(self, locator, keys):
        # `locator` may be None to send keys to active element
        target = self._resolve(locator) if locator else None
        self.sl.press_keys(target, keys)

    # Waits
    def wait_until_visible(self, locator, timeout=None):
        resolved = self._resolve(locator)
        self.sl.wait_until_element_is_visible(resolved, timeout=timeout)

    def wait_until_not_visible(self, locator, timeout=None):
        resolved = self._resolve(locator)
        self.sl.wait_until_element_is_not_visible(resolved, timeout=timeout)

    # CheckBox helpers
    def set_checkbox(self, locator, checked: bool):
        el = self.sl.get_webelement(self._resolve(locator))
        if bool(el.is_selected()) != bool(checked):
            el.click()

    def is_checkbox_selected(self, locator) -> bool:
        el = self.sl.get_webelement(self._resolve(locator))
        return bool(el.is_selected())

    # Listbox helpers
    def get_selected_list_labels(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_selected_list_labels(resolved)

    def get_selected_list_values(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_selected_list_values(resolved)

    # Utility helpers
    def scroll_into_view(self, locator):
        el = self.sl.get_webelement(self._resolve(locator))
        try:
            self.sl.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "nearest"});', el)
        except Exception:
            pass

    def is_enabled(self, locator) -> bool:
        try:
            el = self.sl.get_webelement(self._resolve(locator))
            return bool(el.is_enabled())
        except Exception:
            return False

    def is_editable(self, locator) -> bool:
        try:
            el = self.sl.get_webelement(self._resolve(locator))
            if not el.is_enabled():
                return False
            tag = (el.tag_name or '').lower()
            ce = (el.get_attribute('contenteditable') or '').lower()
            if ce in ('true', 'plaintext-only'):
                return True
            ro = el.get_attribute('readonly')
            if ro is not None and str(ro).lower() not in ('false', 'none'):
                return False
            if tag in ('input', 'textarea'):
                return True
            return False
        except Exception:
            return False

    # Visibility/focusability helpers
    def is_visible(self, locator) -> bool:
        try:
            el = self.sl.get_webelement(self._resolve(locator))
            return bool(el.is_displayed())
        except Exception:
            return False

    def is_focusable(self, locator) -> bool:
        try:
            el = self.sl.get_webelement(self._resolve(locator))
            # must exist; if disabled, not focusable
            if not el.is_enabled():
                return False
            tag = (el.tag_name or '').lower()
            ce = (el.get_attribute('contenteditable') or '').lower()
            if ce in ('true', 'plaintext-only'):
                return True
            # tabindex >= 0 is focusable
            tb = el.get_attribute('tabindex')
            if tb is not None:
                try:
                    if int(str(tb)) >= 0:
                        return True
                except Exception:
                    pass
            # typical natively focusable elements
            if tag in ('input', 'select', 'textarea', 'button'):
                return True
            if tag == 'a':
                href = el.get_attribute('href')
                if href:
                    return True
            return False
        except Exception:
            return False

    def is_clickable(self, locator) -> bool:
        try:
            return bool(self.is_visible(locator) and self.is_enabled(locator))
        except Exception:
            return False

    def unselect_all_from_list(self, locator):
        resolved = self._resolve(locator)
        self.sl.unselect_all_from_list(resolved)

    def unselect_from_list_by_label(self, locator, labels):
        resolved = self._resolve(locator)
        self.sl.unselect_from_list_by_label(resolved, labels)

    def unselect_from_list_by_value(self, locator, values):
        resolved = self._resolve(locator)
        self.sl.unselect_from_list_by_value(resolved, values)

    # Radio helpers
    def select_radio(self, group_name: str, value: str):
        self.sl.select_radio_button(group_name, value)

    def radio_button_should_be_set_to(self, group_name: str, value: str):
        self.sl.radio_button_should_be_set_to(group_name, value)

    def _resolve(self, locator_dict):
        if not locator_dict:
            raise ValueError("Locator missing")
        if isinstance(locator_dict, str):
            return locator_dict
        if isinstance(locator_dict, dict):
            if len(locator_dict) != 1:
                raise ValueError(f"Locator must have exactly one key, got: {locator_dict}")
            key, value = list(locator_dict.items())[0]
            return f"{key}:{value}"
        raise TypeError(f"Unsupported locator format: {locator_dict}")

    # Focus helpers
    def focus(self, locator):
        el = self.sl.get_webelement(self._resolve(locator))
        try:
            # Prefer JS focus to avoid scrolling/click side effects
            self.sl.driver.execute_script('arguments[0].focus();', el)
        except Exception:
            # Fallback: click element
            el.click()

    def has_focus(self, locator) -> bool:
        el = self.sl.get_webelement(self._resolve(locator))
        try:
            active = self.sl.driver.switch_to.active_element
            return el == active
        except Exception:
            return False
