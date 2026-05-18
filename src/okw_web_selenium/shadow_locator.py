"""ShadowLocator -- Wrapper for locators inside Shadow DOM.

Carries the shadow host chain alongside the element locator.
The adapter detects this type in ``_resolve()`` and navigates
through shadow roots before finding the target element.

YAML example (single shadow host)::

    ShadowButton:
      class: okw_web_selenium.widgets.webse_button.WebSe_Button
      shadow_host: { css: '#shadow-host' }
      locator: { css: '#my-btn' }

YAML example (nested shadow hosts)::

    DeepElement:
      class: okw_web_selenium.widgets.webse_label.WebSe_Label
      shadow_host:
        - { css: '#outer-host' }
        - { css: '#inner-host' }
      locator: { css: '.target' }

Note: Only CSS selectors work inside Shadow DOM.
XPath is not supported by the browser's Shadow Root API.
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
