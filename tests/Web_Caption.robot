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
    SetOKWParameter    TimeOutVerifyCaption    10
    SetValue       URL         ${FILE_URL}
    StartApp      WidgetsDemo

Teardown Widgets Demo
    StopHost

*** Test Cases ***
Verify Button Caption
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    VerifyCaption      OK      OK
    Teardown Widgets Demo

Memorize And Log Caption
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    MemorizeCaption    OK      OkCaption
    LogCaption         OK
    Teardown Widgets Demo

