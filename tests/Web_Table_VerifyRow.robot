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
Header And Row Content
    Setup Table Demo
    SelectWindow   TableDemo
    # Header row (row=0)
    VerifyTableRowContent    DemoTable    0    Col1$TABCol2$TABCol3
    # Row 2 with empty middle cell
    VerifyTableRowContent    DemoTable    2    A21$TAB$EMPTY$TABA23
    Teardown Table Demo


