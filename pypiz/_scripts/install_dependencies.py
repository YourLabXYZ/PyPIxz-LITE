# (c) 2024 YourLabXYZ.
# Licensed under MIT License.

import os
import logging
import subprocess
import sys


def install_packages(file_path="requirements.txt", enable_logging=False):
    """
    Installs all packages listed in a requirements.txt file.

    :param file_path: Path to the requirements.txt file (default is "requirements.txt").
    :param enable_logging: enable logging (default is False).
    """

    file_path = os.path.abspath(file_path)

    # Check if the file exists and is valid
    if not os.path.isfile(file_path):
        message = f"The {file_path} file was not found."
        logging.error(message) if enable_logging else print(message)
        raise FileNotFoundError(message)

    try:
        # Run the pip install -r requirements.txt command
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", file_path],
            check=True,  # Raises CalledProcessError if the command fails
            capture_output=True,  # Captures stdout and stderr for debugging/logging
            text=True  # Decodes stdout/stderr as text
        )

        success_message = "Successfully installed dependencies."
        logging.info(success_message) if not enable_logging else print(success_message)

        # Optionally log the output for debugging
        if enable_logging:
            logging.debug("Command output:\n%s", result.stdout)

    except subprocess.CalledProcessError as error:
        # Handle installation errors
        error_message = f"An error occurred while installing dependencies: {error.stderr or 'Unknown error'}"
        logging.error(error_message) if enable_logging else print(error_message)
        raise EnvironmentError(error_message) from error
