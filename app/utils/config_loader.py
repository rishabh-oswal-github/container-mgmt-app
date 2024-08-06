import yaml
from pathlib import Path

def load_config():
    config_path = Path(__file__).parent.parent / "config.yml"
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config
