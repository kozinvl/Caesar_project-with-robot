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
    Go To    http://localhost:3000/admin
    Click Button    css:.btn.btn-warning.home
    Title Should Be    Caesar    It isn't Group Page
    Close Browser

Checking title Admin page after login which was successful
    [Tags]    Admin Page
    Login with arguments    qwerty    1234
    Go To    http://localhost:3000/admin
    Page Should Contain    Caesar Admin Panel    It isn't Admin Page
    Close Browser

Checking User's second name after creating
    [Tags]    Admin Page3
    Login with arguments    qwerty    1234
    Go To    http://localhost:3000/admin
    Tab users
    Add User
    Fill user fields    User    Vasiliy    Teacher    Dnipro    photo    123
    ...    123
    Submit Button
    Page Should Contain    Vasiliy    User wasn't created
    Close Browser

Checking Group name after creating
    Login with arguments    qwerty    1234
    Tab groups
    Add Group
