from robot.api.deco import keyword
from okw4robot.runtime.context import context


class WebKeywords:
    """Selenium-specific keywords for web automation."""

    @keyword("ExecuteJS")
    def execute_js(self, script: str):
        """Executes raw JavaScript in the current browser context.

        Arguments:
        - ``script``: JavaScript source to execute. Must be a self-contained string.

        Behavior:
        - Supported with web adapters that expose SeleniumLibrary as ``adapter.sl``.
          Internally calls ``SeleniumLibrary.Execute Javascript`` and returns its result.

        Examples:
        | ${title}= | ExecuteJS | return document.title; |
        | ${len}=   | ExecuteJS | return document.querySelectorAll('input').length; |
        | ExecuteJS | document.querySelector('#email').value = 'user@example.com'; |
        """
        adapter = context.get_adapter()
        if hasattr(adapter, 'sl') and hasattr(adapter.sl, 'execute_javascript'):
            return adapter.sl.execute_javascript(script)
        a = adapter.__class__.__name__
        raise RuntimeError(f"[ExecuteJS] Not supported by adapter '{a}'")
