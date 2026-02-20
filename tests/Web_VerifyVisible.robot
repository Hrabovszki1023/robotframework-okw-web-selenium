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
    SetValue    URL         ${FILE_URL}
    StartApp      WidgetsDemo

Teardown Widgets Demo
    StopHost

*** Test Cases ***
Visible YES And NO
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyIsVisible   Name        YES
    ExecuteJS    document.querySelector('[data-testid="tf-vorname"]').style.display='none';
    VerifyIsVisible   Vorname     NO
    Teardown Widgets Demo



