from setuptools import setup, find_packages
from typing import List
from pathlib import Path

HYPEN_E_DOT = '-e .'
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


__version__ = "0.0.1"
REPO_NAME = "Python_Pakaging"
PKG_NAME= "db_connect"
AUTHOR_USER_NAME = "rushikeshkusare"
AUTHOR_EMAIL = "rushikeshkkusare29@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirements(Path("requirements_dev.txt"))
    )