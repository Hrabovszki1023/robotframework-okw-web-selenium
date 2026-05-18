"""Locator wrappers for elements behind isolation boundaries.

These wrappers carry extra context (shadow host chain, iframe locator)
alongside the normal element locator.  ``WebSe_Base.__init__`` creates
them automatically when the YAML entry contains ``shadow_host`` or
``iframe``.  The adapter detects the wrapper type in ``_resolve()``
and uses the appropriate traversal strategy.

YAML example -- Shadow DOM (CSS only)::

    ShadowButton:
      class: okw_web_selenium.widgets.webse_button.WebSe_Button
      shadow_host: { css: '#shadow-host' }
      locator: { css: '#my-btn' }

YAML example -- nested Shadow DOM::

    DeepElement:
      class: okw_web_selenium.widgets.webse_label.WebSe_Label
      shadow_host:
        - { css: '#outer-host' }
        - { css: '#inner-host' }
      locator: { css: '.target' }

YAML example -- iFrame (XPath and CSS supported)::

    EmailInput:
      class: okw_web_selenium.widgets.webse_textfield.WebSe_TextField
      iframe: { id: email-subscribe }
      locator: { id: email }

Note: Only CSS selectors work inside Shadow DOM (browser limitation).
iFrames support both CSS and XPath -- no restrictions.
"""


class ShadowLocator:
    """Transparent wrapper: shadow host chain + element locator.

    Created automatically by ``WebSe_Base.__init__`` when the YAML
    entry contains a ``shadow_host`` key.  The test writer and all
    widget subclasses never see this type -- they keep using
    ``self.locator`` as before.
    """

    __slots__ = ("shadow_hosts", "element_locator")

    def __init__(self, shadow_hosts, element_locator):
        if isinstance(shadow_hosts, list):
            self.shadow_hosts = shadow_hosts
        else:
            self.shadow_hosts = [shadow_hosts]
        self.element_locator = element_locator

    def __bool__(self):
        return bool(self.element_locator)

    def __repr__(self):
        return (
            f"ShadowLocator(hosts={self.shadow_hosts}, "
            f"locator={self.element_locator})"
        )


class IFrameLocator:
    """Transparent wrapper: iframe locator + element locator.

    Created automatically by ``WebSe_Base.__init__`` when the YAML
    entry contains an ``iframe`` key.  The adapter switches into the
    frame before finding the element and switches back to
    ``default_content`` afterwards.

    Unlike Shadow DOM, iFrames support both CSS and XPath selectors.
    """

    __slots__ = ("iframe_locator", "element_locator")

    def __init__(self, iframe_locator, element_locator):
        self.iframe_locator = iframe_locator
        self.element_locator = element_locator

    def __bool__(self):
        return bool(self.element_locator)

    def __repr__(self):
        return (
            f"IFrameLocator(iframe={self.iframe_locator}, "
            f"locator={self.element_locator})"
        )
