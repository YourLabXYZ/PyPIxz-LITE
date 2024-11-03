# (c) 2024 KDUser12.
# Licensed under the MIT License.

import os


def clear_output():
    command = 'cls' if os.name == 'nt' else 'clear'
    return os.system(command)
