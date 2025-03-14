1. ###Installation###
#Clone the Repository
git clone https://github.com/mystikyatra
cd web-app-automation-pogo

#Install pip
Windows : Download python from https://www.python.org/downloads/windows/

#Run in your project terminal
python -m ensurepip --default-pip

#Check python version
python3 --version

#Install the required libraries in requiremensts.txt
pip install -r requirements.txt

#Upgrade python to latest version if available
python.exe -m pip install --upgrade pip

#Setup the virtual environment : For Windows
python -m venv venv
venv\Scripts\activate

#Install WebDriver for Chrome
python -c "from webdriver_manager.chrome import ChromeDriverManager; print(ChromeDriverManager().install())"

#Run all tests
pytest -v

#Run a specific test file : For Login, Game Search, ToolTip Validation and Logout.
pytest tests/test_login.py -v

#Run this file for user registration
#Notes : When registration run through automation, Puzzle is displayed to verify its human interaction, which can't be automated. #On normal registration it is not displayed.
pytest tests/test_registration.py -v









