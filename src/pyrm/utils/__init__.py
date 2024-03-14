import subprocess


def run(commmand: list[str]) -> str:
    return subprocess.check_output(commmand).decode().strip()


def create_venv() -> None:
    run(["python3", "-m", "venv", ".venv"])


def get_requirements() -> str:
    """
    Cast pip freeze output to dict

    freeze outputs string of package==version pairs separated by newlines
    """
    reqs = run(["python3", "-m", "pip", "freeze"])
    return dict([pkg.split("==") for pkg in reqs.splitlines()])


def get_git_user() -> str:
    return run(["git", "config", "user.name"])


def get_git_email() -> str:
    return run(["git", "config", "user.email"])


def install(): ...


print(get_requirements())
