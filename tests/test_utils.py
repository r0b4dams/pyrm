import os
import tempfile
from src.pyrob.utils import create_venv

def test_create_venv():
    with tempfile.TemporaryDirectory() as tmpdirname:
        create_venv(tmpdirname)
        assert os.path.exists(tmpdirname)
        assert os.path.exists(f"{tmpdirname}/bin/python3")
