from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements. 
    Read requirements.txt file, append each in requirement_list variable and return the list.

    """
    requirement_list:List[str] = []

    # with open("requirements.txt", 'r') as reqfile:
    #     lines = reqfile.readlines()

    # for line in lines:
    #     if (not line.startswith('#')):
    #         line = line.strip('\n')
    #         print(line)
    #         requirement_list.append(line)

    return requirement_list  

setup(
    name="sensor",
    version="0.0.1",
    author="ThetaMindz",
    author_email="vvktyagi@gmail.com",
    packages = find_packages(),
    #install_requires=["pymongo==4.2.0"],
    install_requires=get_requirements(),
)

