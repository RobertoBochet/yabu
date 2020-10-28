import logging
from shutil import which

from yabu import exceptions
import yaml

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
        pass

    @staticmethod
    def _check_tools() -> None:
        if which("rsync") is None:
            raise exceptions.RsyncNotAvailable()
