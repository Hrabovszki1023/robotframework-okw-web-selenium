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
Clickable YES And NO
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyIsClickable   OK      YES
    ExecuteJS    document.querySelector('[data-testid="btn-ok"]').style.display='none';
    VerifyIsClickable   OK      NO
    Teardown Widgets Demo



