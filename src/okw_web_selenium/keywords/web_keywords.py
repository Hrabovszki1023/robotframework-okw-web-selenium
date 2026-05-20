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

    _DEFAULT_AD_SELECTORS = [
        'iframe[id*="ad"]',
        'iframe[id*="google_ads"]',
        'iframe[src*="googlesyndication"]',
        'iframe[src*="doubleclick"]',
        'ins.adsbygoogle',
        'div[id*="google_ads"]',
    ]

    @keyword("RemoveAds")
    def remove_ads(self, *selectors):
        """Removes ad elements from the current page via JavaScript.

        Without arguments, removes common Google Ads iframes and containers.
        With arguments, each argument is a CSS selector targeting elements
        to remove.

        Arguments:
        - ``*selectors``: CSS selectors (optional). Defaults to Google Ads selectors.

        Examples:
        | RemoveAds |
        | RemoveAds | iframe[src*="googlesyndication"] | ins.adsbygoogle |
        | OnFailIgnoreNOISE | RemoveAds |
        | OnFailIgnoreNOISE | RemoveAds | div.custom-ad-banner |
        """
        adapter = context.get_adapter()
        if not (hasattr(adapter, 'sl') and hasattr(adapter.sl, 'execute_javascript')):
            a = adapter.__class__.__name__
            raise RuntimeError(f"[RemoveAds] Not supported by adapter '{a}'")

        css_list = list(selectors) if selectors else self._DEFAULT_AD_SELECTORS
        combined = ", ".join(css_list)
        script = """
            var selector = arguments[0];
            var removed = 0;
            document.querySelectorAll(selector)
                .forEach(function(el) { el.remove(); removed++; });

            if (!window._okwAdObserver) {
                window._okwAdObserver = new MutationObserver(function(mutations) {
                    mutations.forEach(function(m) {
                        m.addedNodes.forEach(function(node) {
                            if (node.nodeType === 1) {
                                if (node.matches && node.matches(selector)) {
                                    node.remove();
                                }
                                node.querySelectorAll && node.querySelectorAll(selector)
                                    .forEach(function(el) { el.remove(); });
                            }
                        });
                    });
                });
                window._okwAdObserver.observe(document.body, {childList: true, subtree: true});
            }
            return removed;
        """
        count = adapter.sl.execute_javascript(script, combined)
        from robot.api import logger
        logger.info(f"[RemoveAds] {count} existing element(s) removed. "
                    f"MutationObserver active for: {combined}")
