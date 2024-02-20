# pyrob

A CLI to manage dependencies in a Python project

# Usage

| Command           | Description                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| `pyrob init`      | Initialize a new project and generate starter files                                                      |
| `pyrob install`   | Install given packages to virtual environment. If no args given, install packages listed in project.json |
| `pyrob uninstall` | Unistall packages from virtual environment                                                               |
| `pyrob run`       | Run the given script. If no arg given, run main                                                          |
| `pyrob clean`     | Remove pycache artifacts and virtual environment                                                         |

# Development

| Command            | Description                               |
| ------------------ | ----------------------------------------- |
| `make`             | Build wheel and sdist                     |
| `make install`     | Install package to pip globally           |
| `make uninstall`   | Uninstall package from pip                |
| `make version`     | Set version (e.g. `make version v=1.2.3`) |
| `make clean`       | Remove dev, build and cache artifacts     |
| `make upload_test` | Publish package to TestPyPI               |
