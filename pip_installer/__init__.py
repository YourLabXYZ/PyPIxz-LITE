# (c) 2024 YourLabXYZ.
# Licensed under MIT License.

""" PIP-Installer

PIP-Installer is a program to help developers and users to better manage
the dependencies required for the proper functioning of their program.
"""

from ._scripts.install_dependencies import install_packages

__version__ = 'release-1.0'
__all__ = [
    'install_packages'
]

__author__ = 'YourLabXYZ'
