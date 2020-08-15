""" setup for gitignore project."""

from os import path
from setuptools import setup
import pathlib


# here = path.abspath(path.dirname(__file__))
HERE = pathlib.Path(__file__).parent

# Get the long description from the README file
README = (HERE/"README.md").read_text()

setup(
    name="git-autoignore",
    version="1.0.3",
    description="Create gitignore template with lighten Speed",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Imdeepmehta/git-autoignore",
    author="Imdeepmehta",
    license='MIT',
    author_email="itsdeepmehta25@gmail.com",
    packages=["gitignore"],
    include_package_data = True,
    
    install_requires=[
        "requests",
        "beautifulsoup4",
        "lxml",
    ],
    entry_points={
        "console_scripts": [
            "git-autoignore = gitignore.__main__:main"
        ]
    },
)
