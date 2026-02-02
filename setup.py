#responsible for building the whole project as a package so that anyone can use it 
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
#returns a list of requirement(list of libraries)
def get_requirements(file_path:str)->List[str]: 

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() 
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Divy',
author_email='divymakwana100@gmail.com',
packages=find_packages(), #whenever find packages run it will see the source as a package and find __init__.py 
# install_require=['pandas','numpy','seaborn'],
install_requires=get_requirements('requirements.txt')
)
