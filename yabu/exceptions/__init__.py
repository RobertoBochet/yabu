class YABUerror(Exception):
    pass


class RsyncNotAvailable(YABUerror):
    def __str__(self) -> str:
        return "'rsync' tool not found"


class ConfigError(YABUerror):
    pass


class ConfigNotFound(ConfigError):
    def __init__(self, file: str):
        self._file = file

    def __str__(self) -> str:
        return "Configuration file '{}' not found".format(self._file)


class InvalidConfig(ConfigError):
    pass
