class RsyncNotAvailable(Exception):
    pass


class ConfigError(Exception):
    pass


class ConfigNotFound(ConfigError):
    pass


class InvalidConfig(ConfigError):
    pass
