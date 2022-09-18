from setuptools import setup
from typing import List

    
# declaring variable for setup functions
PROJECT_NAME= "housing-predictor-project"
VERSION="0.0.1"
AUTHOR="Khushboo Singh"
DESCRIPTION="This is the first end to end project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]: #This function will return the list which have string value in it
    with open(REQUIREMENT_FILE_NAME) as  requirement_file:
        requireme_file.readlines().remove("-e .")

setup(
name = PROJECT_NAME,
version= VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires = get_requirements_list()
)
