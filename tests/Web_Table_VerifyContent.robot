*** Settings ***
Library    okw_web_selenium.library.OkwWebSeleniumLibrary


*** Variables ***
${DEMO_FILE}    docs/examples/table_demo.html

*** Keywords ***
Setup Table Demo
    StartHost     Chrome
    StartApp      Chrome
    SelectWindow  Chrome
    ${FILE_URL}=   Evaluate    __import__('pathlib').Path('${DEMO_FILE}').resolve().as_uri()
    SetValue    URL         ${FILE_URL}
    StartApp      TableDemo

Teardown Table Demo
    StopHost

*** Test Cases ***
Whole Table Matches
    Setup Table Demo
    SelectWindow   TableDemo
    ${pattern}=    Set Variable    A11$TABA12$TABA13$LFA21$TAB$EMPTY$TABA23$LFA31$TABA32$TABA33
    VerifyTableContent    DemoTable    ${pattern}
    Teardown Table Demo


