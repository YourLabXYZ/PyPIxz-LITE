# Changelog

Any notable changes to PyPIz will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Added a display of log output.
- Added a new function allowing you to install a module with a specific version (optional).
- Added a new function allowing you to know information about a module and a specific version of the module (optional).

### Changed

- Changed the name of the "logger" parameter to "enable logging" of the "install_packages" function.
- Changed the method of calling a command via Subprocess.
- Changing the log method.
- Changed file name from "install_dependencies.py" to "install_packages.py".

## [1.0.2] - 2024-12-01

### Added

- Added a CHANGELOG.md file to monitor the progress of the project.

### Fixed

-  Fix code scanning alert - Starting a process with a partial executable path #23 

## [1.0.1] - 2024-11-28

### Fixed

- Fix code scanning alert - Consider possible security implications associated with subprocess module. #16 
- Fix code scanning alert - subprocess call - check for execution of untrusted input. #14 
- Fix code scanning alert - Using subprocess.run without explicitly set check is not recommended. (subprocess-run-check) #7 
- Fix code scanning alert - Variable name "e" doesn't conform to snake_case naming style #10 
- Fix code scanning alert - Consider explicitly re-raising using the 'from' keyword #13 
- Fix code scanning alert - Too many arguments for logging format string #3 
- Fix code scanning alert - Use lazy % formatting in logging functions (logging-fstring-interpolation) #8 
- Fix code scanning alert - Trailing newlines #11 
 
[1.0.2]: https://github.com/YourLabXYZ/PyPIz/compare/release/v1.0...release/v1.0.2
[1.0.1]: https://github.com/YourLabXYZ/PyPIz/compare/1.0-release...master