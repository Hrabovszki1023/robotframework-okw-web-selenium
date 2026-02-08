import inspect
from robot.api import logger

class LoggingMixin:
    def log_current_method(self, msg: str = ""):
        """
        Loggt den aktuellen Klassennamen + Methodenname ins Robot-Log.
        Optional mit Zusatznachricht.
        Ausgabe: [Klasse.Methode] Nachricht
        """
        frame = inspect.currentframe().f_back
        method = frame.f_code.co_name
        class_name = self.__class__.__name__
        log_line = f"[{class_name}.{method}] {msg}".strip()
        logger.info(log_line)


    def _debug_print_stack(self):
        """
        Gibt alle Einträge im aktuellen Call-Stack aus –
        hilfreich zur Analyse der Aufruferkette.
        """
        import inspect
        logger.info("\n--- Aktueller Call-Stack ---")
        for i, frame_info in enumerate(inspect.stack()):
            cls_self = frame_info.frame.f_locals.get("self")
            class_part = f"{cls_self.__class__.__name__}." if cls_self else ""
            logger.info(f"{i}: {class_part}{frame_info.function}() in {frame_info.filename}:{frame_info.lineno}")
        logger.info("--- Ende Call-Stack ---\n")

    def _get_caller_method(self):
        stack = inspect.stack()
        if len(stack) < 4:
            return "<unknown>", "<unknown>"
        frame_info = stack[2]
        cls_self = frame_info.frame.f_locals.get("self")
        class_name = cls_self.__class__.__name__ if cls_self else "<unknown>"
        method = frame_info.function
        return class_name, method

    def log_info(self, msg: str):
        class_name, method = self._get_caller_method()
        logger.info(f"[{class_name}.{method}] ℹ️ {msg}")

    def log_warn(self, msg: str):
        class_name, method = self._get_caller_method()
        logger.warn(f"[{class_name}.{method}] ⚠️ {msg}")

    def log_error(self, msg: str):
        class_name, method = self._get_caller_method()
        logger.error(f"[{class_name}.{method}] ❌ {msg}")

    def log_exception(self, msg: str):
        self._debug_print_stack()
        class_name, method = self._get_caller_method()
        logger.error(f"[{class_name}.{method}] 💥{msg}")