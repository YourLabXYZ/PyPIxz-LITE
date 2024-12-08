# (c) 2024 YourLabXYZ.
# Licensed under MIT License.

""" PyPIz

PyPIz is a program to help developers and users to better manage
the dependencies required for the proper functioning of their program.
"""

from pypiz.install_packages import install_requirements, install_modules
from pypiz.pypi_packages import get_module_info

__version__ = 'release-1.1'
__all__ = [
    'install_requirements',
    'install_modules',
    'get_module_info'
]

__author__ = 'YourLabXYZ'
