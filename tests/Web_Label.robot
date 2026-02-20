*** Settings ***
Library    okw_web_selenium.library.OkwWebSeleniumLibrary


*** Variables ***
${DEMO_FILE}    docs/examples/widgets_demo.html

*** Keywords ***
Setup Widgets Demo
    StartHost     Chrome
    StartApp      Chrome
    SelectWindow  Chrome
    ${FILE_URL}=   Evaluate    __import__('pathlib').Path('${DEMO_FILE}').resolve().as_uri()
    SetOKWParameter    TimeOutVerifyLabel    10
    SetOKWParameter    TimeOutVerifyValue    10
    SetValue       URL         ${FILE_URL}
    StartApp      WidgetsDemo

Teardown Widgets Demo
    StopHost

*** Test Cases ***
Verify Labels For Form Controls
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyLabel        Name            Name
    VerifyLabel        Vorname         Vorname
    VerifyLabel        Anmerkung       Anmerkung
    VerifyLabel        Verheiratet     Verheiratet
    VerifyLabel        Geschlecht      Geschlecht
    Teardown Widgets Demo

Label Wildcard And Regex
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyLabelWCM     Verheiratet     *heirat*
    VerifyLabelREGX    Geschlecht      ^Geschl.*
    Teardown Widgets Demo

Memorize And Log Label
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    MemorizeLabel      Name        NameLabel
    LogLabel           Name
    # Verwendung: ${NameLabel}
    Teardown Widgets Demo

