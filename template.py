import os
from pathlib import Path
import logging

package_name = "mongodb_connect"

files_list = [
    # ".github/workflows/.gitkeep",
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    "src/components/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    # "src/components/data_ingestion.py",
    # "src/components/data_transformation.py",
    # "src/components/model_training.py",
    # "src/components/model_evaluation.py",
    # "src/pipeline/__init__.py",
    # "src/pipeline/training_pipeline.py",
    # "src/pipeline/prediction_pipeline.py",
    # "src/utils/utils.py",
    # "src/logger/__init__.py",
    # "src/logger/logging.py",
    # "src/exception/exception.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/integration.py",
    "init_shetup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]


for file in files_list:
    filepath = Path(file)
    file_dir, file_name = os.path.split(filepath)
    if file_dir !='':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0) :
        with open(filepath, 'w') as f:
            pass # Creating an empty file