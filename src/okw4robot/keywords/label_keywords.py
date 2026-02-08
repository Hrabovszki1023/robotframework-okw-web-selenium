from robot.api.deco import keyword
from ..runtime.context import context


def _blank_ignore_enabled() -> bool:
    try:
        from robot.libraries.BuiltIn import BuiltIn
        val = BuiltIn().get_variable_value("${OKW_IGNORE_EMPTY}", default="NO")
        return str(val).strip().upper() in ("YES", "TRUE", "1")
    except Exception:
        return False


def _should_ignore(value) -> bool:
    if isinstance(value, str):
        sv = value.strip()
        t = sv.upper()
        if t in ("$IGNORE", "${IGNORE}"):
            return True
        if sv == "" and _blank_ignore_enabled():
            return True
    return False


def _resolve_widget(name):
    model = context.get_current_window_model()
    if name not in model:
        raise KeyError(f"Widget '{name}' not found in current window.")
    entry = model[name]
    from ..utils.loader import load_class
    widget_class = load_class(entry["class"])
    adapter = context.get_adapter()
    extras = {k: v for k, v in entry.items() if k not in ("class", "locator")}
    return widget_class(adapter, entry.get("locator"), **extras)


def _get_label_text(widget) -> str:
    a = widget.adapter
    # 1) aria-labelledby
    try:
        aria = a.get_attribute(widget.locator, 'aria-labelledby')
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
        elem_id = a.get_attribute(widget.locator, 'id')
        if elem_id:
            try:
                txt = a.get_text({'css': f'label[for="{elem_id}"]'})
                if txt and txt.strip():
                    return txt
            except Exception:
                pass
    except Exception:
        pass
    # 3) aria-label as last resort
    try:
        aria_label = a.get_attribute(widget.locator, 'aria-label')
        if aria_label:
            return aria_label
    except Exception:
        pass
    # 4) fallback to element's own visible text (buttons/links/labels)
    try:
        return a.get_text(widget.locator) or ""
    except Exception:
        return ""


class LabelKeywords:
    def _timeout_seconds(self):
        try:
            from robot.libraries.BuiltIn import BuiltIn
            to = BuiltIn().get_variable_value("${OKW_TIMEOUT_VERIFY_LABEL}", default=10)
            return float(to) if isinstance(to, (int, float)) else BuiltIn().convert_time(str(to))
        except Exception:
            return 10.0

    @keyword("VerifyLabel")
    def verify_label(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyLabel] '{name}' ignored (blank or $IGNORE)")
            return
        import time
        w = _resolve_widget(name)
        end = time.time() + self._timeout_seconds()
        last = None
        while time.time() < end:
            last = _get_label_text(w)
            if last == expected:
                return
            time.sleep(0.1)
        raise AssertionError("[VerifyLabel] Expected '" + str(expected) + "', last seen '" + str(last) + "'")

    @keyword("VerifyLabelWCM")
    def verify_label_wcm(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyLabelWCM] '{name}' ignored (blank or $IGNORE)")
            return
        import time, re
        w = _resolve_widget(name)
        pattern = '^' + re.escape(expected).replace(r'\*', '.*').replace(r'\?', '.') + '$'
        rx = re.compile(pattern, re.DOTALL)
        end = time.time() + self._timeout_seconds()
        last = None
        while time.time() < end:
            last = _get_label_text(w) or ""
            if rx.match(last):
                return
            time.sleep(0.1)
        raise AssertionError("[VerifyLabelWCM] Value '" + str(last) + "' does not match pattern '" + str(expected) + "'")

    @keyword("VerifyLabelREGX")
    def verify_label_regx(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyLabelREGX] '{name}' ignored (blank or $IGNORE)")
            return
        import time, re
        w = _resolve_widget(name)
        end = time.time() + self._timeout_seconds()
        last = None
        while time.time() < end:
            last = _get_label_text(w) or ""
            if re.search(expected, last):
                return
            time.sleep(0.1)
        raise AssertionError("[VerifyLabelREGX] Value '" + str(last) + "' does not match regex '" + str(expected) + "'")

    @keyword("MemorizeLabel")
    def memorize_label(self, name, variable):
        from robot.libraries.BuiltIn import BuiltIn
        w = _resolve_widget(name)
        value = _get_label_text(w)
        var = str(variable).strip()
        if var.startswith("${") and var.endswith("}"):
            var_name = var
        elif var.startswith("$"):
            var_name = "${" + var[1:] + "}"
        else:
            var_name = "${" + var + "}"
        BuiltIn().set_test_variable(var_name, value)

    @keyword("LogLabel")
    def log_label(self, name):
        w = _resolve_widget(name)
        print("LOG:", _get_label_text(w))

