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
Cell Value With WCM
    Setup Table Demo
    SelectWindow   TableDemo
    VerifyTableCellValue    DemoTable    1    3    A1*
    VerifyTableCellValue    DemoTable    2    2    $EMPTY
    Teardown Table Demo


