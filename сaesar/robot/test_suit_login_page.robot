*** Settings ***
Library           Selenium2Library
Resource          open_browser.robot

*** Test Cases ***
Login as Admin
    [Documentation]    Login on Caesar as Admin
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    qwerty
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    Click Element    xpath=//*[@id="icon"]/div/img
    ${User Name}    Get Text    class=name
    ${User Role}    Get Text    class=role
    Should Be Equal    ${User Name}    Kirill\nKozak
    Should Be Equal    ${User Role}    ITA Administrator
    [Teardown]    Close Browser

Login as Teacher
    [Documentation]    Login on Caesar as Admin
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    sasha
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    Click Element    xpath=//*[@id="icon"]/div/img
    ${User Name}    Get Text    class=name
    ${User Role}    Get Text    class=role
    Should Be Equal    ${User Name}    Olexandr\nReuta
    Should Be Equal    ${User Role}    ITA Teacher
    [Teardown]    Close Browser

Login as Coordinator
    [Documentation]    Login on Caesar as Admin
    [Tags]    login
    [Setup]    OpenBrowserCustom    http://localhost:3000/    chrome
    Input Text    name=login    dmytro
    Input Text    name=password    1234
    Click Element    class=submit
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    5    Element user image not found.
    Click Element    xpath=//*[@id="icon"]/div/img
    ${User Name}    Get Text    class=name
    ${User Role}    Get Text    class=role
    Should Be Equal    ${User Name}    Dmytro\nPetin
    Should Be Equal    ${User Role}    ITA Coordinator
    [Teardown]    Close Browser
