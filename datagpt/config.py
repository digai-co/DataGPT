import os

import yaml

from datagpt.util import root


class Config:
    """Usage：
    config = Config("config.yaml")
    secret_key = config.get_key("MY_SECRET_KEY")
    print("Secret key:", secret_key)
    """

    default_yaml_file = root / "config/config.yaml"

    def __init__(self, yaml_file=default_yaml_file):
        self._config = {}
        self.__init_with_config_files_and_env(self._config, yaml_file)

    def __init_with_config_files_and_env(self, configs: dict, yaml_file):
        for _yaml_file in [yaml_file]:
            if not _yaml_file.exists():
                continue

            with open(_yaml_file, "r", encoding="utf-8") as file:
                yaml_data = yaml.safe_load(file)
                if not yaml_data:
                    continue

                configs.update(yaml_data)

        configs.update(os.environ)

    def __lookup(self, dct, key):
        if "." in key:
            key, node = key.split(".", 1)
            return self.__lookup(dct[key], node)
        elif key in dct:
            return dct[key]
        else:
            return None

    def get(self, *keys: str, default=None):
        for key in keys:
            value = self._config.get(key)
            if value is not None:
                return value
            value = self.__lookup(self._config, key)
            if value is not None:
                return value
        return default


config = Config()
