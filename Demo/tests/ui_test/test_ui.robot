*** Settings ***
Library           Selenium2Library
Suite Setup       Open Chrome And Go To Login Page
Suite Teardown    Close Chrome

*** Variables ***
${WEBPAGE}                  http://127.0.0.1:5500/webpage/login.html
${BROWSER}                  chrome
${USER_NAME}                Robot_user
${USER_PASSWORD}            robot_123
${WRONG_USERNAME}           fake_user
${WRONG_PASSWORD}           fake_password
${LOGIN_SUCCESS}            log in success
${LOGIN_FAIL}               log in fail
${NAME_EMPTY_ALERT}         name should not be empty
${PASSWORD_EMPTY_ALERT}     password should not be empty


*** Test Cases ***
Test log in with correct name and password
    # Given open browser and go to login page
    # When
    Input Correct User Name
    Input Correct User Password
    Click Login Button
    # Then
    Show Login Success Alert

Test login with empty name and password
    # Given open browser and go to login page
    # When
    Click Login Button
    # Then
    Show Name Should Not Be Empty Alert

Test login with empty name and correct password
    # Given open browser and go to login page
    # When
    Input Empty Name
    Input Correct User Password
    Click Login Button
    # Then
    Show Name Should Not Be Empty Alert

Test login with correct name and empty password
    # Given open browser and go to login page
    # When
    Input Correct User Name
    Input Empty Password
    Click Login Button
    # Then
    Show Password Should Not Be Empty Alert

Test login with wrong user name and password
    # Given open browser and go to login page
    # When
    Input Wrong Name
    Input Wrong Password
    Click Login Button
    # Then
    Show Login Fail Alert

*** Keywords ***
Open Chrome And Go To Login Page
    Open Browser    ${WEBPAGE}    ${BROWSER}
    Wait Until Element Is Visible    title    3    "the title should be visible in 3 seconds"
    sleep    1s

Close Chrome
    Close Browser
    sleep    1s

Input Correct User Name
    Input Text    name    ${USER_NAME}

Input Correct User Password
    Input Text    password    ${USER_PASSWORD}

Input Empty Name
    Input Text    name    ${EMPTY}

Input Empty Password
    Input Text    password    ${EMPTY}

Input Wrong Name
    Input Text    name    ${WRONG_USERNAME}

Input Wrong Password
    Input Text    password    ${WRONG_PASSWORD}

Click Login Button
    Wait Until Element Is Visible    login-button    3
    Click Button    login-button
    sleep    1s

Show Login Success Alert
    Alert Should Be Present    ${LOGIN_SUCCESS}    ACCEPT

Show Login Fail Alert
    Alert Should Be Present    ${LOGIN_FAIL}    ACCEPT

Show Name Should Not Be Empty Alert
    Alert Should Be Present    ${NAME_EMPTY_ALERT}    ACCEPT

Show Password Should Not Be Empty Alert
    Alert Should Be Present    ${PASSWORD_EMPTY_ALERT}    ACCEPT