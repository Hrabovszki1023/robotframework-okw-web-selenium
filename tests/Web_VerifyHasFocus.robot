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
HasFocus YES And NO
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    SetFocus         Name
    VerifyHasFocus   Name        YES
    VerifyHasFocus   Vorname     NO
    SetFocus         Vorname
    VerifyHasFocus   Name        NO
    VerifyHasFocus   Vorname     YES
    Teardown Widgets Demo


