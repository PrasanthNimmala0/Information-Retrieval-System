import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "test.py",
]

created_dirs = set()  # to avoid duplicate directory creation logs

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:  # only create directory if not empty
        if filedir not in created_dirs:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir}")
            created_dirs.add(filedir)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
