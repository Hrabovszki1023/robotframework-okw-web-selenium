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
List And Selected Counts
    Setup Widgets Demo
    SelectWindow   WidgetsDemo
    # Combo options count (native select has 4 options)
    VerifyListCount        Geschlecht       4
    # Radio group counts: Zahlungsmethode has 3; Lieferung has 5
    VerifyListCount        Zahlungsmethode  3
    VerifyListCount        Lieferung        5
    # Selected count: radios are initially 0; after selecting becomes 1
    VerifySelectedCount    Zahlungsmethode  0
    Select                  Zahlungsmethode  paypal
    VerifySelectedCount    Zahlungsmethode  1
    Teardown Widgets Demo

