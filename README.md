
# PyPIz

**PyPIz** is a simple, modern, and easy-to-use solution for managing your Python dependencies.

[![Contributors](https://img.shields.io/github/contributors/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/pulls)
[![Forks](https://img.shields.io/github/forks/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/network/members)

PyPIz allows you to quickly and efficiently install the dependencies required for your Python programs to run smoothly. It is designed to integrate seamlessly with other modules, such as **logging** for log management, while ensuring compatibility with modern Python environments.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Compatibility](#compatibility)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Install PyPIz directly from PyPI:

```bash
$ python -m pip install pypiz
```

---

## Usage

Here’s a simple example of how to use PyPIz in your project:

```python
import pypiz

# Install dependencies listed in a requirements.txt file
pypiz.install_requirements("requirements.txt", enable_logging=True)  # The "log" argument requires the use
                                                                     # of the "logging" module.
```

- **Parameters**:
  - `requirements.txt`: Path to the file containing your dependencies.
  - `log` *(bool)*: Enables or disables logging.

---

## Features

- **Fast Installation**: Manage your dependencies from a `requirements.txt` file.
- **Modularity**: Compatible with other tools and libraries, such as `logging`.
- **Broad Compatibility**: Supports modern Python versions (3.8+).

---

## Compatibility

PyPIz officially supports **Python 3.8+** : 
- **3.13.x**
- **3.12.x**
- **3.11.x**
- **3.10.x**
- **3.9.x**
- **3.8.x**

---

## Contributing

We welcome contributions from the community! If you'd like to report an issue, propose a new feature, or contribute to 
the development, please check out our [contributing page](https://github.com/yourlabxyz/pypiz/graphs/contributors).

[![Contributors](https://img.shields.io/github/contributors/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/pulls)
[![Forks](https://img.shields.io/github/forks/yourlabxyz/pypiz.svg)](https://github.com/yourlabxyz/pypiz/network/members)

---

## License

This project is licensed under the [MIT License](https://github.com/yourlabxyz/pypiz/blob/master/LICENSE). See 
the license file for more details.

---