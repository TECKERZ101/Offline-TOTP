# Offline-TOTP
## Setup Instructions

> [!NOTE]
> This repo does not contain .ps1 files, instead these files are named without the file extension due to restrictions.

### Prerequisites
1. You will need python and pip installed before starting
2. Install the virtualenv package if not already installed
```
pip install virtualenv
```

### Setup
1. Clone the repo into a folder
2. CD into the cloned repo
3. CD into the exe generator folder
```
cd executable
```
5. Create the python virtual environment
```
ython -m venv env
```
6. Activate the virtual environment using powershell
```
env/Scripts/Activate.ps1
```
8. Install the required packages
```
pip install pyotp pyperclip pyinstaller
```
10. Fill in the otp secret in the main.py file
11. Compile the python file into an exe
```
pyinstaller main.py
```
13. Wait for it to finish compiling.
> [!IMPORTANT]
> The files contained in the executable/bin folder (the folder containing the exe file) are **ALL** needed for the exe to function properly.

### Usage
