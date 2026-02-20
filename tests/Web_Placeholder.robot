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
    SetOKWParameter    TimeOutVerifyPlaceholder    10
    SetValue       URL         ${FILE_URL}
    StartApp      WidgetsDemo

Teardown Widgets Demo
    StopHost

*** Test Cases ***
Verify Placeholders
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyPlaceholder        Name        Nachname
    VerifyPlaceholderWCM     Vorname     *name*
    VerifyPlaceholderREGX    Anmerkung   ^Mehrzeilige\\s+Eingabe.*
    Teardown Widgets Demo

