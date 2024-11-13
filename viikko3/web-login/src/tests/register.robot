*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  lala
    Set Password  lalalala123
    Set Password Confirmation  lalalala123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  la
    Set Password  lalalala123
    Set Password Confirmation  lalalala123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  lala
    Set Password  lala12
    Set Password Confirmation  lala12
    Submit Credentials
    Register Should Fail With Message  Password must at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  lala
    Set Password  lalalala
    Set Password Confirmation  lalalala
    Submit Credentials
    Register Should Fail With Message  Password must include numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  lala
    Set Password  lalalala123
    Set Password Confirmation  alal
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  okok
    Set Password  okokokok123
    Set Password Confirmation  okokokok123
    Submit Credentials
    Register Should Fail With Message  Username already taken

Login After Successful Registration
    Set Username  lala
    Set Password  lalalala123
    Set Password Confirmation  lalalala123
    Submit Credentials
    Register Should Succeed
    To Main Page
    Logout
    Set Username  lala
    Set Password  lalalala123
    Login
    Login Should Succeed

Login After Failed Registration
    Set Username  lala
    Set Password  lala12
    Set Password Confirmation  lala123
    Submit Credentials
    Register Should Fail With Message  Password must at least 8 characters long
    Link Login
    Set Username  lala
    Set Password  lala12
    Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

To Main Page
    Click Link  Continue to main page

Logout
    Click Button  Logout

Login
    Click Button  Login

Link Login
    Click Link  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  okok  okokokok123
    Go To Register Page