*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect password
    Input Credentials    kalle    kalle
    Output Should Contain    Invalid username or password

Login With Nonexistent username    
    Input Credentials    ville    ville123
    Output Should Contain    Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
