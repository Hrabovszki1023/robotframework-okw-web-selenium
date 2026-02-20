"""OKW Web Selenium - Selenium driver for OKW4Robot.

Extends OKW4RobotLibrary with Selenium-specific adapter, browser widgets,
and web-only keywords like ExecuteJS.
"""
from __future__ import annotations

from robot.api.deco import library

from okw4robot.library import OKW4RobotLibrary
from .keywords.web_keywords import WebKeywords


@library(scope="GLOBAL")
class OkwWebSeleniumLibrary(OKW4RobotLibrary, WebKeywords):
    """Selenium-based GUI test automation with OKW4Robot.

    = Overview =

    ``OkwWebSeleniumLibrary`` extends ``OKW4RobotLibrary`` with Selenium-specific
    capabilities: a SeleniumWebAdapter for Chrome/Firefox, browser control widgets
    (URL bar, Maximize Window), and web-only keywords like ``ExecuteJS``.

    All generic OKW4Robot keywords (``SetValue``, ``VerifyValue``, ``ClickOn``, ...)
    are inherited from the base library.

    = Installation =

    | pip install robotframework-okw-web-selenium

    = Import =

    | Library    okw_web_selenium.library.OkwWebSeleniumLibrary

    = Beispiel =

    | StartHost        Chrome
    | StartApp         web/LoginApp
    | SelectWindow     LoginDialog
    | SetValue         Username    admin
    | SetValue         Password    secret
    | ClickOn          OK

    = Abhaengigkeiten =

    - ``robotframework-okw4robot >= 0.4.0``
    - ``selenium >= 4.0``
    """

    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'
    ROBOT_LIBRARY_VERSION = '0.3.0'

    def __init__(self):
        """Initialisiert die OkwWebSeleniumLibrary."""
        pass
