
# PyPIxz LITE

**PyPIxz LITE** is a tool for installing packages for your python programs at launch by removing
various functionality that requires various other modules.

[![Contributors](https://img.shields.io/github/contributors/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/pulls)
[![Forks](https://img.shields.io/github/forks/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/network/members)

PyPIxz LITE allows your users to simply launch your program and the necessary modules will
automatically install quickly and efficiently while maintaining a certain security. It is designed
to be used and compatible with other modules such as **logging** for log management while ensuring
compatibility with any Python environment from version 3.8.

> [!CAUTION]
> You can use PyPIxz LITE with a version of Python lower than 3.8, but we do not guarantee the
> compatibility of the program or its updates or security.

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

Install PyPIxz-LITE :

```bash
$ git clone https://github.com/yourlabxyz/pypixz-lite
```

---

## Usage

Here’s a simple example of how to use PyPIxz-LITE in your project:

> [!IMPORTANT]
> Before starting you must place the `pypixz_lite` folder in your project.

> [!WARNING]
> We recommend using PyPIxz LITE at the very beginning of your program to avoid running into the
> `ModuleNotFoundError` error.

```python
import pypixz_lite

# Install dependencies listed in a requirements.txt file
pypixz_lite.install_requirements("requirements.txt", enable_logging=False)
```

- **Parameters**:
  - `requirements.txt`: Path to the file containing your dependencies.
  - `enable_logging` *(bool)*: Enables or disables logging.

---

## Features

- **Fast Installation**: Manage your dependencies from a `requirements.txt` file.
- **Modularity**: Compatible with other tools and libraries, such as `logging`.
- **Broad Compatibility**: Supports modern Python versions (3.8+).

> Some features are not available via PyPIxz LITE because it requires external dependencies.

---

## Compatibility

PyPIxz LITE officially supports **Python 3.8+** : 
- **3.13.x**
- **3.12.x**
- **3.11.x**
- **3.10.x**
- **3.9.x**
- **3.8.x**

---

## Contributing

We welcome contributions from the community! If you'd like to report an issue, propose a new
feature, or contribute to the development, please check out our
[contributing page](https://github.com/yourlabxyz/PyPIxz-LITE/graphs/contributors).

[![Contributors](https://img.shields.io/github/contributors/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/pulls)
[![Forks](https://img.shields.io/github/forks/yourlabxyz/PyPIxz-LITE.svg)](https://github.com/yourlabxyz/PyPIxz-LITE/network/members)

---

## License

This project is licensed under the
[MIT License](https://github.com/yourlabxyz/PyPIxz-LITE/blob/master/LICENSE). See the license file
for more details.

---