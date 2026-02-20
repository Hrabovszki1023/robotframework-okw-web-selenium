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
Cell By Headers With REGX
    Setup Table Demo
    SelectWindow   TableDemo
    # Row selected by key (WCM on first column), column by exact header name, expected via regex
    VerifyTableCellValueByHeadersREGX    DemoTable    A3*     Col2    ^A3[0-9]$
    # Empty check via $EMPTY in REGX variant
    VerifyTableCellValueByHeadersREGX    DemoTable    A2*     Col2    $EMPTY
    Teardown Table Demo

Row Content By Header With REGX
    Setup Table Demo
    SelectWindow   TableDemo
    # Select unique row via header/value, verify per-cell regex patterns
    VerifyTableRowContentByHeaderREGX    DemoTable    Col1    A31    ^A31$$TAB^A3[0-9]$$TAB^A3[0-9]$
    Teardown Table Demo

Column Content By Header With REGX
    Setup Table Demo
    SelectWindow   TableDemo
    # Select column by exact header name, verify each row via regex
    VerifyTableColumnContentByHeaderREGX    DemoTable    Col3    ^A1[0-9]$$LF^A2[0-9]$$LF^A3[0-9]$
    Teardown Table Demo
