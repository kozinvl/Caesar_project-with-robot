*** Settings ***
Library           Selenium2Library

*** Keywords ***
Login with arguments
    [Arguments]    ${login}    ${password}
    Open Browser    http://localhost:3000    chrome
    Maximize Browser Window
    Input Text    name=login    ${login}
    Input Password    name=password    ${password}
    Click Element    class=submit
    Wait Until Page Contains    My Groups    5

Add User
    Click Button    xpath:.//*[text()='Add user']

Fill user fields
    [Arguments]    ${name}    ${last_name}    ${role}    ${location}    ${photo}    ${login}
    ...    ${password}
    Wait Until Element Is Visible    name:firstName    10
    Input Text    name:firstName    ${name}
    Input Text    name:lastName    ${last_name}
    Select From List By Label    name:role    ${role}
    Select From List By Label    name:location    ${location}
    Input Text    name:photo    ${photo}
    Input Text    name:login    ${login}
    Input Text    name:password    ${password}

Tab users
    Click Element    css:a[href*='users']

Submit Button
    Click Button    css:.btn.btn-primary.submit

Add Group
    Click Button    xpath:/.//*[text()='Add group']

Tab groups
    Click Element    css:a[href*='groups

Fill group fields
