# (c) 2024 YourLabXYZ.
# Licensed under MIT License.

import os
import logging
import subprocess


def install_packages(file_path="requirements.txt", logger=False):
    """
    Installs all packages listed in a requirements.txt file.

    :param file_path: Path to the requirements.txt file (default is "requirements.txt").
    :param logger: enable logging (default is False).
    """

    if not os.path.exists(os.path.abspath(file_path)):
        if not logger:
            raise FileNotFoundError(f"The {file_path} file was not found.")
        return logging.error(f"The {file_path} file was not found.")

    try:
        # Run the pip install -r requirements.txt command
        result = subprocess.run(["pip", "install", "-r", file_path])

        if not logger:
            print("Successfully installed dependencies.")
            return print(result.stdout)
        logging.info("Successfully installed dependencies.")
        return logging.info(result.stdout)
    except subprocess.CalledProcessError as e:
        if not logger:
            raise EnvironmentError("An error occurred while installing dependencies.", e.stderr)
        return logging.error("An error occurred while installing dependencies.", e.stderr)


