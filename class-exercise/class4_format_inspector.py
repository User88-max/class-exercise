import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s %(levelname)-8s %(message)s",
    datefmt = "%H:%M:%S"
)
logger = logging.getLogger(__name__)

def inspect_csv(filepath):
    """Read a CSV file and display basic information"""
    df = pd.read_csv(filepath)
    logger.info("CSV file is loaded")
    print(df.head(3))

def inspect_json(filepath):
    """Read a JSON file and display basic information"""
    with open(filepath, "r") as f:
        data = json.load(f)
    logger.info("JSON file is loaded")
    print(data["Status"])
    print(data["Count"])
    print(data["Data"])

def inspect_yaml(filepath):
    """Read a YAML file and display basic information"""
    with open(filepath, "r") as f:
        config = yaml.safe_load(f)
    logger.info("YAML file is loaded")
    print(config["cleaning"]["missing"])
    print(config["processing"]["batch_size"])

def inspect_env():
    """Read a .env file and display basic information"""
    load_dotenv()
    keys = [key for key in ["USERNAME", "PASSWORD"] if os.getenv(key) is not None]
    logger.info(".env file is loaded")
    print(keys)

def main():
    file_path = Path("data")
    file_path_csv = file_path / "sample.csv"
    file_path_json = file_path / "sample.json"
    file_path_yaml = file_path / "sample.yaml"

    inspect_csv(file_path_csv)
    inspect_json(file_path_json)
    inspect_yaml(file_path_yaml)
    inspect_env()

if __name__ == "__main__":
    main()