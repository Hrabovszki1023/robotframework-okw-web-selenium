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
Row And Column Counts
    Setup Table Demo
    SelectWindow   TableDemo
    VerifyTableRowCount       DemoTable    3
    VerifyTableColumnCount    DemoTable    3
    Teardown Table Demo


