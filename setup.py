from setuptools import setup,find_packages
from typing import List

def get_requirements()->List:
    """
    Function Will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty line an -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        raise FileNotFoundError("requirements.txt not found")
    
    return requirement_lst

setup(
    name='ML Project-2',
    version='0.0.1',
    author='Meet Agrawal',
    author_email='maagrawal2112@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
        