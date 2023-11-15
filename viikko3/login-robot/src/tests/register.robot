*** Settings ***
Resource  resource.robot
Test Setup   Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    janne    janne123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    ville    password111
    Output Should Contain    User with username ville already exists

Register With Too Short Username And Valid Password
    Input Credentials   aa   validpw123
    Output Should Contain   Username should be at least 3 characters long (a-z)

Register With Long Enough But Invalid Username And Valid Password
    Input Credentials   aa1aa   validpw123
    Output Should Contain   Username should be at least 3 characters long (a-z)

Register With Valid Username And Too Short Password
    Input Credentials   hessu   short1
    Output Should Contain    Password should be at least 8 characters long and not consist of only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials   hessu   onlylettershere
    Output Should Contain    Password should be at least 8 characters long and not consist of only letters

*** Keywords ***
Create User And Input New Command
    Create User    ville    ville123
    Input New Command