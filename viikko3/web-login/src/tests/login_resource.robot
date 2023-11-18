*** Settings ***
Resource  resource.robot
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Keywords ***
Set Credentials And Login
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Login Credentials

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}