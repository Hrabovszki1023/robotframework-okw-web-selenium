"""WebSe_Base -- Gemeinsame Basis fuer alle Selenium-Web-Widgets.

Implementiert die ``OkwWidget``-Schnittstelle mit Selenium-spezifischer Logik:
- Zustandspruefungen (exists, visible, enabled, editable, focus, ...)
- Attribut-Zugriff (get_attribute, get_text, get_tooltip, get_label, get_placeholder)
- Sync-Helfer (_wait_before) aus dem alten BaseWidget uebernommen
"""

import time
from okw4robot.widgets.okw_widget import OkwWidget
from robot.libraries.BuiltIn import BuiltIn


class WebSe_Base(OkwWidget):
    """Basis fuer alle Selenium-Web-Widgets."""

    def __init__(self, adapter, locator, **options):
        shadow_host = options.pop('shadow_host', None)
        iframe = options.pop('iframe', None)
        if shadow_host and locator:
            from okw_web_selenium.shadow_locator import ShadowLocator
            locator = ShadowLocator(shadow_host, locator)
        elif iframe and locator:
            from okw_web_selenium.shadow_locator import IFrameLocator
            locator = IFrameLocator(iframe, locator)
        super().__init__(adapter, locator, **options)
        self.sl = adapter.sl  # SeleniumLibrary-Instanz

    # ------------------------------------------------------------------
    # Screenshot (Base64)
    # ------------------------------------------------------------------
    def okw_get_screenshot_base64(self) -> "str | None":
        try:
            el = self.sl.get_webelement(self.adapter._resolve(self.locator))
            return el.screenshot_as_base64
        except Exception:
            return None

    # ------------------------------------------------------------------
    # Interaktion (gemeinsam)
    # ------------------------------------------------------------------
    def okw_click(self):
        self._wait_before('write')
        self.adapter.click(self.locator)

    def okw_double_click(self):
        self._wait_before('write')
        self.adapter.double_click(self.locator)

    def okw_move_over(self):
        self._wait_before('read')
        self.adapter.move_over(self.locator)

    def okw_delete(self):
        """Loescht den Feldinhalt: clear + Backspace-Fallback."""
        self._wait_before('write')
        try:
            self.adapter.clear_text(self.locator)
        except Exception:
            pass
        # Fallback: Ctrl+A + Delete
        try:
            self.adapter.press_keys(self.locator, "CTRL+a")
            self.adapter.press_keys(self.locator, "DELETE")
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Drag & Drop (collect → execute pattern)
    # DragStart/DragOver only collect — Drop executes atomically.
    # ------------------------------------------------------------------
    def okw_drag_start(self):
        self._wait_before('read')
        self.adapter.drag_start(self.locator)

    def okw_drag_over(self):
        self._wait_before('read')
        self.adapter.drag_over(self.locator)

    def okw_drop(self):
        self._wait_before('read')
        self.adapter.drop(self.locator)

    # ------------------------------------------------------------------
    # Werte lesen (gemeinsam)
    # ------------------------------------------------------------------
    def okw_get_text(self) -> str:
        return self.adapter.get_text(self.locator) or ""

    def okw_get_attribute(self, name: str) -> str:
        val = self.adapter.get_attribute(self.locator, name)
        return "" if val is None else str(val)

    def okw_get_tooltip(self) -> str:
        """Liest Tooltip: bevorzugt 'title', Fallback 'aria-label'."""
        try:
            val = self.adapter.get_attribute(self.locator, 'title')
            if val:
                return val
        except Exception:
            pass
        try:
            val = self.adapter.get_attribute(self.locator, 'aria-label')
            if val:
                return val
        except Exception:
            pass
        return ""

    def okw_get_label(self) -> str:
        """Liest Label: aria-labelledby -> label[for] -> aria-label -> sichtbarer Text."""
        a = self.adapter
        # 1) aria-labelledby
        try:
            aria = a.get_attribute(self.locator, 'aria-labelledby')
            if aria:
                parts = [p for p in str(aria).split() if p]
                texts = []
                for pid in parts:
                    try:
                        texts.append(a.get_text({'id': pid}) or '')
                    except Exception:
                        pass
                joined = ' '.join(t.strip() for t in texts if t is not None)
                if joined.strip():
                    return joined
        except Exception:
            pass
        # 2) <label for="id">
        try:
            elem_id = a.get_attribute(self.locator, 'id')
            if elem_id:
                try:
                    txt = a.get_text({'css': f'label[for="{elem_id}"]'})
                    if txt and txt.strip():
                        return txt
                except Exception:
                    pass
        except Exception:
            pass
        # 3) aria-label
        try:
            aria_label = a.get_attribute(self.locator, 'aria-label')
            if aria_label:
                return aria_label
        except Exception:
            pass
        # 4) Fallback: sichtbarer Text
        try:
            return a.get_text(self.locator) or ""
        except Exception:
            return ""

    def okw_get_placeholder(self) -> str:
        try:
            ph = self.adapter.get_attribute(self.locator, 'placeholder')
            return ph if ph is not None else ""
        except Exception:
            return ""

    # ------------------------------------------------------------------
    # Zustand (gemeinsam)
    # ------------------------------------------------------------------
    def okw_exists(self) -> bool:
        return self.adapter.element_exists(self.locator)

    def okw_is_visible(self) -> bool:
        return self.adapter.is_visible(self.locator)

    def okw_is_enabled(self) -> bool:
        return self.adapter.is_enabled(self.locator)

    def okw_is_editable(self) -> bool:
        return self.adapter.is_editable(self.locator)

    def okw_has_focus(self) -> bool:
        return self.adapter.has_focus(self.locator)

    def okw_is_focusable(self) -> bool:
        return self.adapter.is_focusable(self.locator)

    def okw_is_clickable(self) -> bool:
        return self.adapter.is_clickable(self.locator)

    def okw_set_focus(self):
        self.adapter.focus(self.locator)

    # ------------------------------------------------------------------
    # Sync-Helfer (aus altem BaseWidget uebernommen)
    # ------------------------------------------------------------------
    def _get_global_sync(self, intent: str) -> dict:
        bi = BuiltIn()
        timeout = bi.get_variable_value(
            '${OKW_SYNC_TIMEOUT_WRITE}' if intent == 'write' else '${OKW_SYNC_TIMEOUT_READ}',
            default=10)
        poll = bi.get_variable_value('${OKW_SYNC_POLL}', default=0.1)
        scroll_def = bi.get_variable_value('${OKW_SYNC_SCROLL_INTO_VIEW}', default='YES')
        editable_def = bi.get_variable_value('${OKW_SYNC_CHECK_EDITABLE}', default='YES')
        busy = bi.get_variable_value(
            '${OKW_BUSY_SELECTORS_WRITE}' if intent == 'write' else '${OKW_BUSY_SELECTORS_READ}',
            default=None)
        busy_list = []
        if busy:
            if isinstance(busy, (list, tuple)):
                busy_list = list(busy)
            else:
                busy_list = [v.strip() for v in str(busy).split(',') if v.strip()]
        return {
            'timeout': float(timeout) if isinstance(timeout, (int, float)) else bi.convert_time(str(timeout)),
            'poll': float(poll) if isinstance(poll, (int, float)) else bi.convert_time(str(poll)),
            'exists': True,
            'visible': True,
            'enabled': True,
            'editable': (
                self.__class__.__name__ in ('WebSe_TextField', 'WebSe_MultilineField')
                and str(editable_def).strip().upper() in ('YES', 'TRUE', '1')
            ) if intent == 'write' else False,
            'scroll_into_view': (
                str(scroll_def).strip().upper() in ('YES', 'TRUE', '1')
            ) if intent == 'write' else False,
            'until_not_visible': busy_list,
        }

    def _merge_wait(self, intent: str) -> dict:
        cfg = self._get_global_sync(intent)
        inst = (self.options.get('wait') or {}).get(intent, {})
        for k, v in inst.items():
            cfg[k] = v
        return cfg

    def _wait_before(self, intent: str):
        cfg = self._merge_wait(intent)
        timeout = float(cfg.get('timeout', 10))
        poll = float(cfg.get('poll', 0.1))
        end = time.time() + timeout
        has_locator = bool(self.locator)

        if has_locator:
            # 1) exists
            if cfg.get('exists', True):
                ok = False
                while time.time() < end:
                    if self.adapter.element_exists(self.locator):
                        ok = True
                        break
                    time.sleep(poll)
                if not ok:
                    raise AssertionError('[Sync] Element does not exist')

            # 2) scroll into view
            if cfg.get('scroll_into_view', False):
                try:
                    self.adapter.scroll_into_view(self.locator)
                except Exception:
                    pass

            # 3) visible
            if cfg.get('visible', True):
                try:
                    self.adapter.wait_until_visible(self.locator, timeout=timeout)
                except Exception:
                    raise AssertionError('[Sync] Element not visible')

            # 4) enabled
            if cfg.get('enabled', True):
                ok = False
                while time.time() < end:
                    if getattr(self.adapter, 'is_enabled', None) and self.adapter.is_enabled(self.locator):
                        ok = True
                        break
                    time.sleep(poll)
                if not ok:
                    raise AssertionError('[Sync] Element not enabled')

            # 5) editable
            if cfg.get('editable', False):
                ok = False
                while time.time() < end:
                    if getattr(self.adapter, 'is_editable', None) and self.adapter.is_editable(self.locator):
                        ok = True
                        break
                    time.sleep(poll)
                if not ok:
                    raise AssertionError('[Sync] Element not editable')

        # 6) project waits (until_not_visible)
        for sel in cfg.get('until_not_visible', []) or []:
            try:
                loc = sel if isinstance(sel, (str, dict)) else str(sel)
                if isinstance(loc, str) and ':' not in loc:
                    loc = {'css': loc}
                self.adapter.wait_until_not_visible(loc, timeout=timeout)
            except Exception:
                pass
