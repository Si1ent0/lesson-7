import os.path
import pytest


CURRENT_FILE = os.path.abspath(__file__)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)

CMD_DIR = os.path.join(CURRENT_DIR, "cmd")

RES_DIR = os.path.join(CURRENT_DIR, "resources")

ARCH_ZIP= os.path.join(RES_DIR, "test_archive.zip")


@pytest.fixture()
def create_folder():
    if not os.path.exists('resources'):
        os.mkdir('resources')