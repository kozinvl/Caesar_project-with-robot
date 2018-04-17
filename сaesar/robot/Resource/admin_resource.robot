*** Settings ***
Library           Selenium2Library

*** Variables ***
${LOGIN URL}      http://localhost:3000/
${BROWSER}        chrome
${ADMIN URL}      http://localhost:3000/admin

*** Keywords ***
Login with arguments
    [Arguments]    ${login}    ${password}
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    name=login    ${login}
    Input Password    name=password    ${password}
    Click Element    class=submit
    Wait Until Page Contains    My Groups    10    Element hasn't been found

Add User
    Click Button    xpath:.//*[text()='Add user']
    Set Selenium Timeout    2

Fill user fields
    [Arguments]    ${name}    ${last_name}    ${role}    ${location}    ${photo}    ${login}
    ...    ${password}
    Wait Until Element Is Visible    name:firstName    15    Element hasn't been found
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
    Set Selenium Timeout    2

Tab groups
    Click Element    css:a[href*='groups']

Fill group fields
    [Arguments]    ${name}    ${location}    ${direction}    ${start_date}    ${finish_date}    ${teachers}
    ...    ${experts}    ${stage}
    Wait Until Element Is Visible    name:stage    10    Element hasn't been found
    Input Text    name:name    ${name}
    Select From List By Label    name:location    ${location}
    Select From List By Label    name:direction    ${direction}
    Press Key    name:startDate    ${start_date}
    Press Key    name:finishDate    ${finish_date}
    Input Text    name:teachers    ${teachers}
    Input Text    name:experts    ${experts}
    Select From List    name:stage    ${stage}

Fill student fields
    [Arguments]    ${group_id}    ${name}    ${last_name}    ${english_level}    ${cv}    ${image}
    ...    ${entry_score}    ${approved_by}
    Wait Until Element Is Visible    name:approvedBy    10    Element hasn't been found
    Input Text    name:groupId    ${group_id}
    Input Text    name:name    ${name}
    Input Text    name:lastName    ${last_name}
    Select From List By Label    name:englishLevel    ${english_level}
    Input Text    name:CvUrl    ${cv}
    Input Text    name:imageUrl    ${image}
    Input Text    name:entryScore    ${entry_score}
    Input Text    name:approvedBy    ${approved_by}

Add Student
    Click Button    xpath:.//*[text()='Add student']
    Set Selenium Timeout    2

Tab students
    Click Element    css:a[href*='students']
