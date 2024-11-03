# (c) 2024 KDUser12.
# Licensed under the MIT License.

import logging
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from __init__ import __longname__, __shortname__, __version__
from Modules._os import check_os_compatibility
from Modules.venv import check_python_version
from Modules.package import check_and_install_dependencies
from Core import PIPInstaller


def setup_logging(debug=False):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('logs.log', mode='a')
        ]
    )

if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, description=f"{__longname__} (Version {__version__})")
    parser.add_argument("-v", "--version", action="version", version=f"{__shortname__} v{__version__}", help="display version information and dependencies")
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="display extra debugging information and metrics")
    parser.add_argument("-s", "--safemode", action='store_true', default=False, help="launches the program without any verification")

    args = parser.parse_args()
    setup_logging(args.debug)

    if not args.safemode:
        try:
            check_os_compatibility()
            check_python_version(['3.8'])
            check_and_install_dependencies(['requirements.txt'])
        except EnvironmentError as error:
            exit(logging.error(f"Error: {error}"))

    PIPInstaller(args.debug)
