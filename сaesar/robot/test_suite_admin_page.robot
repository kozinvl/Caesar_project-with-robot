*** Settings ***
Documentation     Test suite to testing admin's page
Suite Setup
Force Tags
Library           Selenium2Library
Resource          Resource/resource.robot

*** Test Cases ***
Check title Group page after clicking home button at Admin Page
    [Tags]    Admin Page
    [Timeout]
    Login as Administrator
    Go To    http://localhost:3000/admin
    Click Button    css:.btn.btn-warning.home
    Title Should Be    Caesar
    Close Browser
