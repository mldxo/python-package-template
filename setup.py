"""Setup file for the python package template"""

from setuptools import setup, find_packages
from python_package_template.version import __version__ as version

with open("README.md", "r") as file:
    description = file.read()

setup(
    name = "python-package-template",
    version = version,
    packages = find_packages(),
    install_requires = [
        #"your-dependency",
    ],
    entry_points = {
        "console_scripts" : [
            "python-package-template = python_package_template:main",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)
