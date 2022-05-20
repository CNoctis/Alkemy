from scripts.download import main as download
from scripts.update_db import main as update_db


if __name__ == '__main__':
    download()
    update_db()