import os
from src.pyrob.utils import create_venv
from src.pyrob.config.vars import VENV


def test_create_env():
    create_venv(VENV)
    assert os.path.exists(VENV)
    assert os.path.exists(f"{VENV}/bin/python3")
