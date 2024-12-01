# (c) 2024 YourLabXYZ.
# Licensed under MIT License.

import os
import logging
import subprocess
import sys


def install_packages(file_path="requirements.txt", logger=False):
    """
    Installs all packages listed in a requirements.txt file.

    :param file_path: Path to the requirements.txt file (default is "requirements.txt").
    :param logger: enable logging (default is False).
    """

    if not os.path.isfile(os.path.abspath(file_path)):
        if not logger:
            raise FileNotFoundError(f"The {file_path} file was not found.")
        return logging.error("The %s file was not found.", file_path)

    try:
        # Run the pip install -r requirements.txt command
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", os.path.abspath(file_path)])

        if not logger:
            return print("Successfully installed dependencies.")
        return logging.info("Successfully installed dependencies.")
    except subprocess.CalledProcessError as error:
        if not logger:
            raise EnvironmentError("An error occurred while installing dependencies.",
                                   error.stderr) from error
        return logging.error("An error occurred while installing dependencies: %s", error.stderr)
