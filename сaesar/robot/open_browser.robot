*** Settings ***
Library           Selenium2Library

*** Keywords ***
OpenBrowserCustom
    [Arguments]    ${url}    ${browser}
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
