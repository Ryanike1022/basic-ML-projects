from setuptools import find_packages, setup
from typing import List

DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if DOT in requirements:
            requirements.remove(DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Polumati Ryan Ike',
author_email='ryanike.polumati@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)