from setuptools import find_packages, setup
from typing import List

HYPHON_DOT_E = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Description: This function is going to return list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHON_DOT_E in requirements:
            requirements.remove(HYPHON_DOT_E)

    return requirements

setup(
    name = 'MLOps_project_1',
    version = '0.0.1',
    author = "Jaya_Krishna",
    author_email = 'jayakrishna.8000@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)