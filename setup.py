# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="Ashik Shezan",
    description="This is simple number convertion tool. A sample package for python package structure demonstration",
    name="converter",
    packages=find_packages(include=['unit_converter', 'unit_converter.*']),
    version="0.1.0",
    install_requires=['numpy>=1.10', 'pandas'],
)
