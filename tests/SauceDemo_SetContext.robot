*** Settings ***
Library    okw_web_selenium.library.OkwWebSeleniumLibrary

*** Variables ***
${URL}    https://www.saucedemo.com

*** Keywords ***
Anmelden
    [Arguments]    ${benutzer}    ${passwort}
    SelectWindow       SauceDemoLogin
    SetValue           Benutzer    ${benutzer}
    SetValue           Passwort    ${passwort}
    ClickOn            Anmelden

Produktpreis Pruefen
    [Arguments]    ${produkt}    ${erwarteter_preis}
    [Documentation]    Prueft den Preis eines Produkts ueber SetContext.
    SetContext         ProduktKarte    ${produkt}
    VerifyValue        Produktpreis    ${erwarteter_preis}

Produkt In Warenkorb Legen
    [Arguments]    ${produkt}
    [Documentation]    Legt ein Produkt ueber SetContext in den Warenkorb.
    SetContext         ProduktKarte    ${produkt}
    ClickOn            InDenWarenkorb

*** Test Cases ***
SetContext Produktpreise Pruefen
    [Documentation]    Testet SetContext mit SauceDemo Produktkarten.
    ...    Prueft Preise verschiedener Produkte ohne separate YAML-Eintraege.
    StartApp       MyAppChrome
    SelectWindow   Chrome
    SetValue       URL    ${URL}
    Anmelden       standard_user    secret_sauce
    SelectWindow   SauceDemoProducts
    VerifyValue    Titel    Products
    Produktpreis Pruefen    Sauce Labs Backpack      $29.99
    Produktpreis Pruefen    Sauce Labs Bike Light    $9.99
    Produktpreis Pruefen    Sauce Labs Bolt T-Shirt  $15.99
    StopApp        MyAppChrome

SetContext Produkt In Warenkorb
    [Documentation]    Testet SetContext mit Klick-Aktion auf Produktkarte.
    StartApp       MyAppChrome
    SelectWindow   Chrome
    SetValue       URL    ${URL}
    Anmelden       standard_user    secret_sauce
    SelectWindow   SauceDemoProducts
    Produkt In Warenkorb Legen    Sauce Labs Backpack
    Produkt In Warenkorb Legen    Sauce Labs Bike Light
    StopApp        MyAppChrome
