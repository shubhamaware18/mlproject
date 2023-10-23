from setuptools import find_packages, setup  # Import necessary functions from setuptools
from typing import List  # Import the List type from the typing module

HYPEN_E_DOT='-e .'  # Define a constant string

# Define a function called get_requirements that takes a file path as input
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements=[]  # Initialize an empty list to store requirements
    with open(file_path) as file_obj:  # Open the file specified by file_path
        requirements=file_obj.readlines()  # Read the lines from the file into the requirements list
        requirements=[req.replace("\n","") for req in requirements]  # Remove newline characters from each requirement

        if HYPEN_E_DOT in requirements:  # If '-e .' is found in the requirements list
            requirements.remove(HYPEN_E_DOT)  # Remove it from the list of requirements
    
    return requirements  # Return the list of requirements

# Define the package setup information using setup function
setup(
    name    = 'mlproject',  # Name of the package
    version = '0.0.1',  # Version number
    author  = 'Shubham',  # Author's name
    author_email='awareshubham1996@gmail.com',  # Author's email address
    packages=find_packages(),  # Automatically discover and include all packages in the distribution
    install_requires=get_requirements('requirements.txt')  # List of package dependencies from requirements.txt file
)
