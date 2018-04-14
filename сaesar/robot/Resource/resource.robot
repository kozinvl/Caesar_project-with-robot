*** Settings ***
Library           Selenium2Library

*** Keywords ***
Login as Administrator
    Open Browser    http://localhost:3000    chrome
    Maximize Browser Window
    Input Text    name=login    qwerty
    Input Password    name=password    1234
    Click Element    class=submit
