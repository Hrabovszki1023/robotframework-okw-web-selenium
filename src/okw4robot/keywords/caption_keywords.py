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


def _get_caption_text(widget) -> str:
    # Caption = sichtbarer Text des Elements selbst
    try:
        return widget.adapter.get_text(widget.locator) or ""
    except Exception:
        return ""


class CaptionKeywords:
    def _timeout_seconds(self):
        try:
            from robot.libraries.BuiltIn import BuiltIn
            to = BuiltIn().get_variable_value("${OKW_TIMEOUT_VERIFY_CAPTION}", default=10)
            return float(to) if isinstance(to, (int, float)) else BuiltIn().convert_time(str(to))
        except Exception:
            return 10.0

    @keyword("VerifyCaption")
    def verify_caption(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyCaption] '{name}' ignored (blank or $IGNORE)")
            return
        import time
        w = _resolve_widget(name)
        end = time.time() + self._timeout_seconds()
        last = None
        while time.time() < end:
            last = _get_caption_text(w)
            if last == expected:
                return
            time.sleep(0.1)
        raise AssertionError("[VerifyCaption] Expected '" + str(expected) + "', last seen '" + str(last) + "'")

    @keyword("VerifyCaptionWCM")
    def verify_caption_wcm(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyCaptionWCM] '{name}' ignored (blank or $IGNORE)")
            return
        import time, re
        w = _resolve_widget(name)
        pattern = '^' + re.escape(expected).replace(r'\\*', '.*').replace(r'\\?', '.') + '$'
        rx = re.compile(pattern, re.DOTALL)
        end = time.time() + self._timeout_seconds()
        last = None
        while time.time() < end:
            last = _get_caption_text(w) or ""
            if rx.match(last):
                return
            time.sleep(0.1)
        raise AssertionError("[VerifyCaptionWCM] Value '" + str(last) + "' does not match pattern '" + str(expected) + "'")

    @keyword("VerifyCaptionREGX")
    def verify_caption_regx(self, name, expected):
        if _should_ignore(expected):
            print(f"[VerifyCaptionREGX] '{name}' ignored (blank or $IGNORE)")
            return
        import time, re
        w = _resolve_widget(name)
        end = time.time() + self._timeout_seconds()
        last = None
        while time.time() < end:
            last = _get_caption_text(w) or ""
            if re.search(expected, last):
                return
            time.sleep(0.1)
        raise AssertionError("[VerifyCaptionREGX] Value '" + str(last) + "' does not match regex '" + str(expected) + "'")

    @keyword("MemorizeCaption")
    def memorize_caption(self, name, variable):
        from robot.libraries.BuiltIn import BuiltIn
        w = _resolve_widget(name)
        value = _get_caption_text(w)
        var = str(variable).strip()
        if var.startswith("${") and var.endswith("}"):
            var_name = var
        elif var.startswith("$"):
            var_name = "${" + var[1:] + "}"
        else:
            var_name = "${" + var + "}"
        BuiltIn().set_test_variable(var_name, value)

    @keyword("LogCaption")
    def log_caption(self, name):
        w = _resolve_widget(name)
        print("LOG:", _get_caption_text(w))

