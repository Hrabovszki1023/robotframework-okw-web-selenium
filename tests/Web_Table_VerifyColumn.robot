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
Column Content With $LF
    Setup Table Demo
    SelectWindow   TableDemo
    VerifyTableColumnContent    DemoTable    1    A11$LFA21$LFA31
    VerifyTableColumnContent    DemoTable    2    A12$LF$EMPTY$LFA32
    Teardown Table Demo


