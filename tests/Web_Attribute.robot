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
    SetOKWParameter    TimeOutVerifyAttribute    10
    SetValue       URL         ${FILE_URL}
    StartApp      WidgetsDemo

Teardown Widgets Demo
    StopHost

*** Test Cases ***
Verify Placeholder Attributes
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyAttribute       Name        placeholder    Nachname
    VerifyAttributeWCM    Vorname     placeholder    *name*
    VerifyAttributeREGX   Anmerkung   placeholder    ^Mehrzeilige\\s+Eingabe.*
    Teardown Widgets Demo

Verify And Memorize Data Attributes
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyAttribute       OK          data-testid     btn-ok
    MemorizeAttribute     OK          data-testid     OkDataTest
    LogAttribute          OK          data-testid
    Teardown Widgets Demo


