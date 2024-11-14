# Subprocess Execution

*Efficient library for running Python code in isolated subprocesses.*

[![PyPI Version](https://img.shields.io/pypi/v/your-library-name.svg)](https://pypi.org/project/your-library-name/)
[![Build Status](https://github.com/yourusername/your-library-name/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/your-library-name/actions)
[![License](https://img.shields.io/github/license/yourusername/your-library-name)](https://github.com/yourusername/your-library-name/blob/main/LICENSE)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [From Source](#from-source)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Examples](#examples)
- [Documentation](#documentation)
- [License](#license)
- [Contact](#contact)

---

## Overview

This library provides a simple and efficient way to execute arbitrary Python functions in subprocesses, while seamlessly relaying runtime information back to the main process. It is especially useful for diagnosing and resolving system issues that might otherwise crash the Python interpreter.

Designed with minimal dependencies and an intuitive interface, this library makes it easy to execute any Python callable in a robust and straightforward manner.


## Installation

### From PyPI

Install the library using `pip`:

```bash
pip install subprocess-execution
```

### From Source

Clone the repository and install:

```bash
git clone https://github.com/joshwadd/subprocess-execution.git
cd subprocess-execution
pip install .
```

## Usage
