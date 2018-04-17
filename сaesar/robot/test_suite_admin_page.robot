*** Settings ***
Documentation     Test suite to testing admin's page
Suite Setup
Force Tags
Default Tags      Admin Page
Library           Selenium2Library
Resource          Resource/admin_resource.robot

*** Test Cases ***
Checking title Group page after clicking home button at Admin Page
    [Tags]    Admin Page
    [Timeout]
    Login with arguments    qwerty    1234
    Go To    ${ADMIN URL}
    Click Button    css:.btn.btn-warning.home
    Title Should Be    Caesar    It isn't Group Page
    [Teardown]    Close Browser

Checking title Admin page after login which was successful
    [Tags]    Admin Page
    Login with arguments    qwerty    1234
    Go To    ${ADMIN URL}
    Page Should Contain    Caesar Admin Panel    It isn't Admin Page
    [Teardown]    Close Browser

Checking User's second name after creating
    [Tags]    Admin Page
    Login with arguments    qwerty    1234
    Go To    ${ADMIN URL}
    Tab users
    Add User
    Fill user fields    Somebody    Vasiliy    Teacher    Dnipro    photo    123
    ...    123
    Submit Button
    Page Should Contain    Somebody    User's name hasn't been created
    Page Should Contain    Vasiliy    User's second name hasn't been created
    [Teardown]    Close Browser

Checking Group's name after creating
    [Tags]    Admin Page
    Login with arguments    qwerty    1234
    Go To    ${ADMIN URL}
    Tab groups
    Add Group
    Fill group fields    DP-99-JS    Dnipro    MQC    2018-05-15    2018-07-15    D. Petin
    ...    M. Omel`chuk    planned
    Submit Button
    Page Should Contain    DP-99-JS    Group hasn't been created
    [Teardown]    Close Browser

Checking Student's name after creating
    [Tags]    Admin Page
    Login with arguments    qwerty    1234
    Go To    ${ADMIN URL}
    Tab students
    Add Student
    Fill student fields    DP-10-JS    Victor    Caesar    Pre-intermediate    1    1
    ...    99    N. Varenko
    Submit Button
    Page Should Contain    DP-10-JS    Student's id group hasn't been created
    Page Should Contain    Victor    Student's name hasn't been created
    Page Should Contain    Caesar    Student's second name hasn't been created
    [Teardown]    Close Browser

Checking Submit button after filling "Student" fields with symbol
    [Tags]    Admin Page
    Login with arguments    qwerty    1234
    Go to    ${ADMIN URL}
    Tab students
    Add Student
    Fill student fields    '    '    '    Pre-intermediate    '    '
    ...    '    '
    Element Should Be Disabled    css:.btn.btn-primary.submit
    [Teardown]    Close Browser

Checking button after filling "User" fields with symbols more than max length
    [Tags]    A
    Login with arguments    qwerty    1234
    Go To    ${ADMIN URL}
    Tab users
    Add User
    Fill user fields    Coder    Developerovich    Teacher    Dnipro    photo    aaaaaaaaaaa
    ...    bbbbbbbbbbb
    Element Should Be Disabled    css:.btn.btn-primary.submit
    [Teardown]    Close Browser

Checking button after filling "User" login & password with special symbols
    Login with arguments    qwerty    1234
    Go To    ${ADMIN URL}
    Tab users
    Add User
    Fill user fields    Vasyl    Petrovich    Teacher    Dnipro    photo    !!!!!!
    ...    ;;;;;;
