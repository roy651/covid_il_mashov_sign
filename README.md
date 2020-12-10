# covid-il-mashov-sign
(work-in-progress)
### Prerequisites
- Firefox browser

### Setup
- Clone or download zip
- Run 'pip install -r requirements.txt'
- Credentials:
    - Either create a 'creds' file with each of the values to the below credentials (without the var names). Each value in a separate line in the exact order as below
    - Or create environment variables with the below names:
        - MAIL_USER - your gmail username (usually address)
        - MAIL_PASS - your gmail password
        - MOE_USER - your username to the mashov login page
        - MOE_PASS - your password to the above
        - MOE_SCHOOL - school code in the mashov system
    - Or pass them in CLI to the run command as in the example below
- Note that this package includes the gecko driver to mac 
    - If you need a windows/linux driver download it download it here: https://github.com/mozilla/geckodriver/releases
    - Alternatively you can provide the path to the geckodriver on your os using env var GECKODRIVER_PATH
- Also - you may specify the path to the firefox binary using FIREFOX_BIN

### System behaviour
- The script will launch a headless Firefox. 
- It will login to the Mashov website and then sign on the button and logout. 
- Actually - because I have 2 kids in this school - it will switch kids and sign on the second kid as well - so for a single kid - simply comment out blocks #21 and #22 in the main.py file
- When finished, the script will report by email what were the results. 
- Note that you can't sign the statement more than once a day - hence on any subsequent run, on the same day, the system will fail due to "already signed" and send the email with a failure message.

### Run locally
python main.py {mail-user} {mail-pass} {mashov-login} {mashov-pass} {mashov-school-code}

### Run on Heroku
- After setting up a python dyno using a python buildpack and pushing the project to heroku you'll need to add the below buildpack which includes the gecko driver and FF:
`heroku buildpacks:add https://github.com/roy651/heroku-integrated-firefox-geckodriver`
- You'll probably need to define all the config (env) vars properly as described in the other repsitory:

**FIREFOX_BIN**: */app/vendor/firefox/firefox*

**GECKODRIVER_PATH**: */app/vendor/geckodriver/geckodriver*

**LD_LIBRARY_PATH**: */usr/local/lib:/usr/lib:/lib:/app/vendor*

**PATH**: */usr/local/bin:/usr/bin:/bin:/app/vendor/*

- Finally - It is recommended to assign a Heroku scheduler in order to run a daily job at ~7:00 AM and launch the script


#### For any inquiries - drop me a note and I'll try to explain.
