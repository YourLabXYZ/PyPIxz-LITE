# (c) 2024 KDUser12.
# Licensed under the MIT License.

import platform
import sys
import calendar
from datetime import datetime

from __init__ import __version__
from Modules.update import check_versions
from Core.Management.Commands.basic_commands import clear_output


class PIPInstaller:
    def __init__(self, debug=False):
        self.current_version = __version__
        self.latest_version = check_versions(self.current_version)

        self.operating_system = platform.system()
        self.python_version = '.'.join(map(str, sys.version_info[:3]))
        self.current_time = datetime.now()

        clear_output()

        print(f"PIP-Installer - {self.current_version}{" [DEBUG-MODE]" if debug else ""} (main, {calendar.month_abbr[self.current_time.month]}"
              f" {self.current_time.day} {self.current_time.year}, {self.current_time.hour}:{self.current_time.minute}) [Python "
              f"{self.python_version}] on {self.operating_system}\nFor more information enter \"help\", \"license\" or \"credit\".\n")

        if self.latest_version:
            print("Install the latest YourLabs for new features and improvements! https://github.com/KDUser12/YourLabs/releases/latest\n")
        elif self.latest_version is None:
            print("An error has occurred, please check that you have the latest version! https://github.com/KDUser12/YourLabs/releases/latest\n")
