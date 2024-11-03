# (c) 2024 KDUser12.
# Licensed under the MIT License.

import logging
import platform
import re


def check_os_compatibility():
    os_name = platform.system()
    os_release = platform.release()

    # Extraction of the Linux kernel version (especially for Arch Linux and similar distros)
    if os_name == 'Linux':
        os_version = extract_kernel_version(os_release)
    else:
        os_version = platform.version()

    logging.debug(f"Detected operating system: {os_name}")
    logging.debug(f"Detected version: {os_version}")
    logging.debug(f"Detected release: {os_release}")

    # Checking supported operating systems
    supported_os = {
        'Windows': {'min_version': '10.0', 'patterns': [r'^[0-9]+\.[0-9]+$']},
        'Linux': {'min_version': '4.0', 'patterns': [r'^[0-9]+\.[0-9]+$', r'^[0-9]+\.[0-9]+\.[0-9]+$']},
        'Darwin': {"min_version": '19.0', 'patterns': [r'^[0-9]+\.[0-9]+$']}
    }

    if os_name not in supported_os:
        raise EnvironmentError(f"Unsupported operating system: {os_name}")

    os_info = supported_os[os_name]
    min_version = os_info['min_version']

    logging.debug(f"Minimum required version for {os_name}: {min_version}")

    # Checking the OS version
    if not any(re.match(pattern, os_version) for pattern in os_info['patterns']):
        raise EnvironmentError(f"Unrecognized OS version: {os_version}")

    if not is_version_compatible(os_version, min_version):
        raise EnvironmentError(f"Minimum required version for {os_name} is {min_version}, but you have {os_version}")

    logging.info(f"Operating system: {os_name} {os_version} ({os_release})")


def extract_kernel_version(os_release):
    # Find the first instance of the version in X.Y.Z or X.Y format.
    match = re.search(r'\d+\.\d+(\.\d+)?', os_release)
    if match:
        kernel_version = match.group(0)
        logging.debug(f"Could not extract kernel version from: {kernel_version}")
        return kernel_version
    else:
        logging.error(f"Could not extract kernel version from: {os_release}")
        return os_release  # Return the original version if no correspondence is found.


def is_version_compatible(current_version, min_version):
    def version_tuple(version_str):
        return tuple(map(int, version_str.split('.')))

    current_version_tuple = version_tuple(current_version)
    min_version_tuple = version_tuple(min_version)

    logging.debug(f"Comparing versions: current ({current_version_tuple}) >= minimum ({min_version_tuple})")

    return current_version_tuple >= min_version_tuple