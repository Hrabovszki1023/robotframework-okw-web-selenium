from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn

class SeleniumWebAdapter:

    def __init__(self, browser):
        self.browser = browser
        self._shutdown_called = False
        self.sl = SeleniumLibrary()
        self._browser_index = self.sl.open_browser("about:blank", browser=self.browser)

    def shutdown(self):
        if self._shutdown_called:
            return
        self._shutdown_called = True
        try:
            self.sl.close_browser()
        except Exception:
            pass

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
        self.sl.double_click_element(resolved)

    def move_over(self, locator):
        from selenium.webdriver.common.action_chains import ActionChains
        el = self.sl.get_webelement(self._resolve(locator))
        ActionChains(self.sl.driver).move_to_element(el).perform()

    def get_text(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_text(resolved)

    def get_value(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_value(resolved)

    def get_attribute(self, locator, name):
        resolved = self._resolve(locator)
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

    def select_by_label(self, locator, label):
        resolved = self._resolve(locator)
        self.sl.select_from_list_by_label(resolved, label)

    def select_by_value(self, locator, value):
        resolved = self._resolve(locator)
        self.sl.select_from_list_by_value(resolved, value)

    def select_by_index(self, locator, index):
        resolved = self._resolve(locator)
        self.sl.select_from_list_by_index(resolved, str(index))

    def press_keys(self, locator, keys):
        target = self._resolve(locator) if locator else None
        self.sl.press_keys(target, keys)

    def wait_until_visible(self, locator, timeout=None):
        resolved = self._resolve(locator)
        self.sl.wait_until_element_is_visible(resolved, timeout=timeout)

    def wait_until_not_visible(self, locator, timeout=None):
        resolved = self._resolve(locator)
        self.sl.wait_until_element_is_not_visible(resolved, timeout=timeout)

    def set_checkbox(self, locator, checked: bool):
        el = self.sl.get_webelement(self._resolve(locator))
        if bool(el.is_selected()) != bool(checked):
            el.click()

    def is_checkbox_selected(self, locator) -> bool:
        el = self.sl.get_webelement(self._resolve(locator))
        return bool(el.is_selected())

    def get_selected_list_labels(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_selected_list_labels(resolved)

    def get_selected_list_values(self, locator):
        resolved = self._resolve(locator)
        return self.sl.get_selected_list_values(resolved)

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

    def is_visible(self, locator) -> bool:
        try:
            el = self.sl.get_webelement(self._resolve(locator))
            return bool(el.is_displayed())
        except Exception:
            return False

    def is_focusable(self, locator) -> bool:
        try:
            el = self.sl.get_webelement(self._resolve(locator))
            if not el.is_enabled():
                return False
            tag = (el.tag_name or '').lower()
            ce = (el.get_attribute('contenteditable') or '').lower()
            if ce in ('true', 'plaintext-only'):
                return True
            tb = el.get_attribute('tabindex')
            if tb is not None:
                try:
                    if int(str(tb)) >= 0:
                        return True
                except Exception:
                    pass
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

    def select_radio(self, group_name: str, value: str):
        self.sl.select_radio_button(group_name, value)

    def radio_button_should_be_set_to(self, group_name: str, value: str):
        self.sl.radio_button_should_be_set_to(group_name, value)

    # ------------------------------------------------------------------
    # iFrame tracking: the adapter remembers which iframe is active
    # and switches only when needed.
    # ------------------------------------------------------------------
    _current_iframe = None  # str key of the currently active iframe

    def _ensure_default_content(self):
        """Switch back to the top-level document if an iframe is active."""
        if self._current_iframe is not None:
            self.sl.driver.switch_to.default_content()
            self._current_iframe = None

    def _resolve(self, locator_dict):
        if not locator_dict:
            raise ValueError("Locator missing")
        # Shadow DOM: navigate through shadow roots, return WebElement
        from okw_web_selenium.shadow_locator import ShadowLocator, IFrameLocator
        if isinstance(locator_dict, ShadowLocator):
            self._ensure_default_content()
            return self._resolve_shadow(locator_dict)
        # iFrame: switch into frame if needed, return locator string
        if isinstance(locator_dict, IFrameLocator):
            return self._resolve_iframe(locator_dict)
        # Normal locator: ensure we are in default content
        self._ensure_default_content()
        # WebElement passthrough (e.g. from shadow resolution)
        from selenium.webdriver.remote.webelement import WebElement
        if isinstance(locator_dict, WebElement):
            return locator_dict
        if isinstance(locator_dict, str):
            return locator_dict
        if isinstance(locator_dict, dict):
            if len(locator_dict) != 1:
                raise ValueError(f"Locator must have exactly one key, got: {locator_dict}")
            key, value = list(locator_dict.items())[0]
            return f"{key}:{value}"
        raise TypeError(f"Unsupported locator format: {locator_dict}")

    def _resolve_shadow(self, shadow_loc):
        """Navigate through shadow host chain and find element via CSS.

        Args:
            shadow_loc: ``ShadowLocator`` with ``shadow_hosts`` (list of
                locator dicts) and ``element_locator`` (dict).

        Returns:
            WebElement inside the deepest shadow root.

        Raises:
            ValueError: if element_locator uses a non-CSS strategy.
        """
        from selenium.webdriver.common.by import By

        driver = self.sl.driver
        root = driver

        for host_loc in shadow_loc.shadow_hosts:
            host_css = list(host_loc.values())[0]
            if root is driver:
                host_el = driver.find_element(By.CSS_SELECTOR, host_css)
            else:
                host_el = root.find_element(By.CSS_SELECTOR, host_css)
            root = host_el.shadow_root

        # Validate: only CSS works inside Shadow DOM
        loc = shadow_loc.element_locator
        strategy = list(loc.keys())[0]
        if strategy not in ("css", "css selector"):
            raise ValueError(
                f"Shadow DOM only supports CSS selectors, got: '{strategy}'. "
                f"XPath is not supported inside Shadow DOM (browser limitation)."
            )
        css_sel = list(loc.values())[0]
        return root.find_element(By.CSS_SELECTOR, css_sel)

    def _resolve_iframe(self, iframe_loc):
        """Switch into the target iframe (if not already there) and
        return the resolved element locator string.

        The adapter stays inside the iframe after this call so that the
        returned locator string can be used by SeleniumLibrary methods
        to find the element.  When a subsequent ``_resolve()`` call
        targets a normal element or a different iframe, the adapter
        switches back automatically.

        Returns:
            Locator string (e.g. ``"id:email"``) — resolved inside
            the active iframe context.
        """
        iframe_key = str(iframe_loc.iframe_locator)

        if self._current_iframe != iframe_key:
            # Switch to correct iframe
            driver = self.sl.driver
            driver.switch_to.default_content()
            iframe_resolved = self._resolve_dict(iframe_loc.iframe_locator)
            iframe_el = self.sl.get_webelement(iframe_resolved)
            driver.switch_to.frame(iframe_el)
            self._current_iframe = iframe_key

        return self._resolve_dict(iframe_loc.element_locator)

    def get_context_screenshot_base64(self, locator_dict) -> "str | None":
        try:
            resolved = self._resolve(locator_dict)
            el = self.sl.get_webelement(resolved)
            return el.screenshot_as_base64
        except Exception:
            return None

    def _resolve_dict(self, locator_dict):
        """Resolve a plain locator dict to a SeleniumLibrary locator string."""
        if isinstance(locator_dict, str):
            return locator_dict
        key, value = list(locator_dict.items())[0]
        return f"{key}:{value}"

    # ------------------------------------------------------------------
    # Drag & Drop (collect → execute pattern)
    #
    # DragStart / DragOver only collect element references.
    # Drop executes the entire drag sequence atomically via JS.
    # ------------------------------------------------------------------
    _drag_source = None        # WebElement: source of the drag
    _drag_intermediates = None  # list[WebElement]: intermediate targets

    def drag_start(self, locator):
        """Collect the source element — no events fired yet."""
        self._drag_source = self.sl.get_webelement(self._resolve(locator))
        self._drag_intermediates = []

    def drag_over(self, locator):
        """Collect an intermediate target — no events fired yet."""
        if self._drag_source is None:
            raise RuntimeError("drag_over() called without active drag — call drag_start() first.")
        el = self.sl.get_webelement(self._resolve(locator))
        self._drag_intermediates.append(el)

    def drop(self, locator):
        """Execute the entire drag sequence atomically via JS events."""
        if self._drag_source is None:
            raise RuntimeError("drop() called without active drag — call drag_start() first.")
        target = self.sl.get_webelement(self._resolve(locator))
        intermediates = self._drag_intermediates or []
        self._exec_drag(self._drag_source, intermediates, target)
        self._drag_source = None
        self._drag_intermediates = None

    def drag_to(self, source_locator, target_locator):
        """Shortcut: drag source directly to target (no intermediates)."""
        src = self.sl.get_webelement(self._resolve(source_locator))
        tgt = self.sl.get_webelement(self._resolve(target_locator))
        self._exec_drag(src, [], tgt)

    def _exec_drag(self, source, intermediates, target):
        """Fire the complete HTML5 drag event sequence via JavaScript.

        Event order: dragstart(src) → [dragenter+dragover(mid)]* →
        dragenter+dragover+drop(tgt) → dragend(src).
        """
        self.sl.driver.execute_script("""
            var src = arguments[0];
            var mids = arguments[1];
            var tgt = arguments[2];

            var dt = new DataTransfer();
            dt.setData('text/plain', src.id || '');

            function fire(el, type) {
                el.dispatchEvent(new DragEvent(type, {
                    bubbles: true, cancelable: true, dataTransfer: dt
                }));
            }

            // 1. dragstart on source
            fire(src, 'dragstart');

            // 2. dragenter + dragover on each intermediate
            for (var i = 0; i < mids.length; i++) {
                fire(mids[i], 'dragenter');
                fire(mids[i], 'dragover');
                fire(mids[i], 'dragleave');
            }

            // 3. drop on target
            fire(tgt, 'dragenter');
            fire(tgt, 'dragover');
            fire(tgt, 'drop');

            // 4. dragend on source
            fire(src, 'dragend');
        """, source, intermediates, target)

    def focus(self, locator):
        el = self.sl.get_webelement(self._resolve(locator))
        try:
            self.sl.driver.execute_script('arguments[0].focus();', el)
        except Exception:
            el.click()

    def has_focus(self, locator) -> bool:
        el = self.sl.get_webelement(self._resolve(locator))
        try:
            active = self.sl.driver.switch_to.active_element
            return el == active
        except Exception:
            return False
