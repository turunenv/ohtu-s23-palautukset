*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page
Test Teardown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Fail With Message  Username should be at least 3 characters long (a-z)

Register With Valid Username And Invalid Password
    Set Username  allu
    Set Password  allu11
    Set Password Confirmation  allu11
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters and not only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  allu
    Set Password  allu1111
    Set Password Confirmation  allu2222
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation did not match

Login After Successful Registration
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Credentials And Login  ville  ville123
    Login Should Succeed


Login After Failed Registration
    Set Username  allu
    Set Password  allu11
    Set Password Confirmation  allu11
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters and not only letters
    Go To Login Page
    Set Credentials And Login  allu  allu11
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Register Page
    Create User   kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}