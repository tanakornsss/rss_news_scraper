import configparser

from path import BASE_DIR


def load_config():
    config = configparser.ConfigParser()

    config_path = BASE_DIR / "config.ini"
    loaded_files = config.read(config_path, encoding="utf-8-sig")

    if not loaded_files:
        raise FileNotFoundError(f"Config file not found: {config_path}")

    required_sections = [
        "REGION",
        "DATABASE",
        "COLLECTOR",
        "SIMILARITY",
    ]

    for section in required_sections:
        if section not in config:
            raise ValueError(
                f"Missing config section: [{section}]"
            )

    return config


CONFIG = load_config()
