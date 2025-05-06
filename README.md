# Offline-TOTP
## Setup Instructions

### Prerequisites
1. You will need python and pip installed before starting
2. Install the virtualenv package if not already installed
`pip install virtualenv`

### Setup
1. Clone the repo into a folder
2. CD into the cloned repo
3. CD into the exe generator folder
`cd executable`
4. Create the python virtual environment
`python -m venv env`
5. Activate the virtual environment using powershell
`env/Scripts/Activate.ps1`
6. Install the required packages
`pip install pyotp pyperclip pyinstaller`
7. Fill in the otp secret in the main.py file
8. Compile the python file into an exe
`pyinstaller main.py`
9. Wait for it to finish compiling.
