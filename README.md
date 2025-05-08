# Offline-TOTP
## Setup Instructions

> [!NOTE]
> This repo does not contain .ps1 files, instead these files are named without the file extension due to restrictions.
> If you are operating using a script restricted environment clone the repo into your local machine and copy to drive after complete setup.

### Prerequisites
1. You will need python and pip installed before starting
2. Install the virtualenv package if not already installed
```
pip install virtualenv
```

### Setup
1. Clone the repo into a folder

2. CD into the cloned repo

3. Create the python virtual environment
```
python -m venv .\executable\env
```

4. Activate the virtual environment using powershell
```
executable\env\Scripts\Activate.ps1
```

5. Install the required packages
```
pip install pyotp pyperclip pyinstaller
```

6. Fill in the otp secret in the main.py file
  
7. Compile the python file into an exe
```
pyinstaller .\executable\main.py
```

8. Wait for it to finish compiling.
> [!IMPORTANT]
> The files contained in the executable/dist folder (the folder containing the exe file) are **ALL** needed for the exe to function properly.

9. Zip the dist folder, either manually or using the provided script
```
powershell type .\zippify|powershell
```

10. The entire repo can now be moved to a script restricted location with the origin exe file removed
> [!WARNING]
> Do not delete the .zip file

### First Run
On the first run of the program on a new machine, run the first run script to install the exe on local machine
```
powershell type .\firstrun|powershell
```

### Usage
To run the program after first run use the run script
```
powershell type .\run|powershell
```
