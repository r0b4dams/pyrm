import os
import shutil
from src.pyrob.utils import create_venv


def test_create_env():
    _, current_folder_name = os.path.split(os.getcwd())
    test_path = f"{current_folder_name}/test_venv"
    create_venv(test_path)
    assert os.path.exists(test_path)
    assert os.path.exists(f"{test_path}/bin/python3")
    shutil.rmtree(test_path)
