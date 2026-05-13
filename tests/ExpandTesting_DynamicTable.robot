*** Settings ***
Library    okw_web_selenium.library.OkwWebSeleniumLibrary

*** Variables ***
${URL}    https://practice.expandtesting.com/dynamic-table

*** Keywords ***
Dynamische Tabelle Pruefen
    [Documentation]    Zeilen und Spalten wechseln bei jedem Laden.
    ...    OKW findet den Wert trotzdem ueber Header + Zeilenname.
    SelectWindow       DynamicTablePage
    MemorizeTableCellValueByHeaders    TaskManager    Chrome    CPU    CHROME_CPU
    VerifyValueWCM     ChromeCpuLabel    *${CHROME_CPU}*

*** Test Cases ***
Dynamic Table Chrome CPU
    StartApp       MyAppChrome
    SelectWindow   Chrome
    SetValue       URL    ${URL}
    Dynamische Tabelle Pruefen
    StopApp        MyAppChrome

Dynamic Table Firefox CPU
    StartApp       MyAppFirefox
    SelectWindow   Firefox
    SetValue       URL    ${URL}
    Dynamische Tabelle Pruefen
    StopApp        MyAppFirefox
