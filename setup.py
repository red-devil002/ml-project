# This file will help me to create my ML model/files as an package that can be used globle and used in devlopment.
# Building your application as a package itself.
from setuptools import find_packages, setup
from typing import List

# New function that calls the file and install them for the project into project env.
def get_requriements(file_path: str) -> List[str]:
    """
        This function will return the list of requirements for the project.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #This will read each line in the file one by one. 
        # While using the above line the function readlines() leaves a "\n" whie moving to next line so to handle it we have....
        [req.replace("\n", " ") for req in requirements] #List comprihension to remove the "\n" from each line.

        # ignore "-e ."
        if '-e .' in requirements:
            requirements.remove('-e .')

        return requirements

#meta data of the project
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = "Swetang Pandit",
    author_email = "swetangpandit@gmail.com",
    packages = find_packages(),
    install_requires = get_requriements('requirements.txt')
)