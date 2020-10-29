import logging
from pprint import pprint
from shutil import which
from os import path

import yamale
from yamale import YamaleError
from yaml.scanner import ScannerError

from yabu import exceptions

_LOGGER = logging.getLogger(__package__)


class YABU:
    def __init__(self, config_path: str):
        # Checks if the necessary system tools are available
        YABU._check_tools()

        # Loads config
        self._load_config(config_path)

    def start(self):
        pass

    def _load_config(self, config_path: str) -> None:
        # Loads the config schema to validate the config
        schema = yamale.make_schema(path.join(path.dirname(__file__), "resources/config.schema.yaml"))

        # Tries to load config file
        try:
            config = yamale.make_data(config_path)
        except FileNotFoundError:
            _LOGGER.error("Configuration file '{}' not found".format(config_path))
            raise exceptions.ConfigNotFound(config_path)
        except ScannerError as e:
            _LOGGER.error("Invalid configuration file '{}'\n{}".format(config_path, e))
            raise exceptions.InvalidConfig(e)

        # Tries to validate the configuration with the schema
        try:
            yamale.validate(schema, config)
        except YamaleError as e:
            _LOGGER.error("Invalid configuration file '{}'\n{}".format(config_path, e))
            raise exceptions.InvalidConfig(e)

        # Saves the config
        self._config = config
        _LOGGER.info("Configuration loaded")

    @staticmethod
    def _check_tools() -> None:
        # Checks if 'rsync' is available
        if which("rsync") is None:
            e = exceptions.RsyncNotAvailable
            _LOGGER.error(e)
            raise e

        _LOGGER.info("All the needed tools are available")
