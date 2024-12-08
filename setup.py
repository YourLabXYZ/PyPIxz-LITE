from setuptools import setup, find_packages

VERSION = '1.1.0'
DESCRIPTION = ('PyPIz is a simple, modern, and easy-to-use solution for managing your Python '
               'dependencies.')

# Setting up
setup(
    name="pypiz",
    version=VERSION,
    author="YourLabXYZ",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'packages', 'modules', 'installer', 'python3', 'pip', 'dependencies',
              'pypi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)