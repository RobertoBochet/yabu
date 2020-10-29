#!/usr/bin/env python3
import argparse
import logging
import sys

from yabu import YABU
from yabu.exceptions import InvalidConfig, ConfigError
from .log import logger_setup

if __name__ == "__main__":
    # Gets inline arguments
    parser = argparse.ArgumentParser(prog="yabu")

    parser.add_argument("-c", "--config", dest="config_path", default="/etc/yabu/config.yaml",
                        help="configuration file path")
    parser.add_argument("-v", dest="log_level", action="count", default=0,
                        help="number of -v defines level of verbosity")
    parser.add_argument("--info", dest="log_level", action="store_const", const=2, help="equal to -vv")
    parser.add_argument("--debug", dest="log_level", action="store_const", const=3, help="equal to -vvv")

    # Parses args
    args = vars(parser.parse_args())

    # Parses the verbosity level
    logger_setup({
                     0: logging.ERROR,
                     1: logging.WARNING,
                     2: logging.INFO,
                     3: logging.DEBUG
                 }[args["log_level"]])

    # Removes no longer necessary log level from args
    del args["log_level"]

    # Creates an instance of YABU
    try:
        yabu = YABU(**args)
    except ConfigError as e:
        print(e)
        sys.exit(1)

    # Starts backup operations
    yabu.start()
