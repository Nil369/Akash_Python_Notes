'''
An environment which is same as the system interpreter but is isolated from the other Python environments on the system. 
To use virtual environments, we write: 

STEP1: pip install virtualenv  # Install the package

We create a new environment using: 
STEP 2: virtualenv myprojectenv # Creates a new venv 
STEP 3: env\Scripts\activate.ps1 # Type this in your Terminal to activate virtual Environment

‘pip freeze’ returns all the package installed in a given python environment along with the versions. 
STEP 4: pip freeze > requirements .txt 

To install the requirements file in your virtual environment write this:
STEP 5: pip install -r requirements.txt  # Installs all packages listed in the requirements.txt file

'''