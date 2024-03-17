# pyrob

A simple CLI to help manage project package requirements

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)

## Installation

```bash
pip install pyrob
```

## Usage

| Command                     | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| `pyrm init [-y]`            | Initialize a new project                              |
| `pyrm run [script]`         | Run the given command defined in project.json         |
| `pyrm install [pkgs ...]`   | Install the given packages to virtual environment     |
| `pyrm uninstall [pkgs ...]` | Uninstall the given packages from virtual environment |

## Development

A Makefile is included with targets to handle dev actions

| Command          | Description                                          |
| ---------------- | ---------------------------------------------------- |
| `make venv`      | Create a virtual environment with `venv` module      |
| `make test`      | Run unit tests with `pytest`                         |
| `make lint`      | Lint using `pylint`                                  |
| `make format`    | Format using `black`                                 |
| `make typecheck` | Typecheck using `mypy`                               |
| `make build`     | Build a binary wheel and a source tarball            |
| `make install`   | Install the package globally                         |
| `make uninstall` | Uninstall package                                    |
| `make clean`     | Delete virtual environment and build/cache artifacts |
