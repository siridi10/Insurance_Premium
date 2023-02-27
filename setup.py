from setuptools import setup
from typing import List

# Declaring for setup function
PROJECT_NAME="insurance predictor"
VERSION="0.0.1"
AUTHOR="SIRIDI"
DESCRIPTION="FIRST MACHINE LEARNING PROJECT"
PACKAGES=["insurancepre"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()-> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list())
