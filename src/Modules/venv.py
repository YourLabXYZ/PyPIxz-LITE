# (c) 2024 KDUser12.
# Licensed under the MIT License.

import sys
import logging


def check_python_version(required_versions):
    current_version = sys.version_info
    current_version_str = '.'.join(map(str, current_version[:3]))
    logging.debug(f"Current version of Python : {current_version_str}")

    for version in required_versions:
        required_versions = tuple(map(int, version.split('.')))
        logging.debug(f"Checking the required version {'.'.join(map(str, required_versions))}")

        if current_version < required_versions:
            raise EnvironmentError(f"Python version required: {'.'.join(map(str, required_versions))}, current version: {current_version_str}")
        else:
            logging.debug(f"Version {'.'.join(map(str, required_versions))} is compatible.")

    logging.info("All required versions are compatible")
