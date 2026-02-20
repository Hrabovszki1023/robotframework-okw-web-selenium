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
Cell By Headers
    Setup Table Demo
    SelectWindow   TableDemo
    # Row selected by key (WCM on first column), column by exact header name
    VerifyTableCellValueByHeaders    DemoTable    A2*     Col3    A23
    VerifyTableCellValueByHeaders    DemoTable    A2*     Col2    $EMPTY
    Teardown Table Demo

Row Content By Header
    Setup Table Demo
    SelectWindow   TableDemo
    # Select unique row via header/value, verify full row pattern
    VerifyTableRowContentByHeader    DemoTable    Col1    A31    A31$TABA32$TABA33
    Teardown Table Demo

Column Content By Header
    Setup Table Demo
    SelectWindow   TableDemo
    # Select column by exact header name, verify data rows
    VerifyTableColumnContentByHeader    DemoTable    Col2    A12$LF$EMPTY$LFA32
    Teardown Table Demo

