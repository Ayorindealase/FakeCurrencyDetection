from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements used

    '''
    Hypen_E='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if Hypen_E in requirements:
            requirements.remove(Hypen_E)
        return requirements

setup(name='CounterfeitDetection',
      version='0.0.1',
      author='AyorindeAlase',
      author_email='alaseayorinde@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
      
      )