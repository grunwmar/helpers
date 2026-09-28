import logging

DEBUG = logging.DEBUG
INFO = logging.INFO
WARN = logging.WARNING
ERROR = logging.ERROR
FATAL = logging.FATAL


def level_map(level: str):
    """Maps level names given as strings to"""
    """ corresponding logging constants. """

    if level is None:
        return None

    return {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "fatal": logging.FATAL,
    }[level.lower()]


def setup_logger(
    name: str = "app_logger",
    log_file: str = "app.log",
    format: str = "%(asctime)s | %(levelname)s: %(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
    filelog_level=logging.DEBUG,
    consolelog_level=logging.DEBUG,
    filelog_format=None,
    consolelog_format=None,
) -> logging.Logger:
    """Setups custom logger."""

    logger = logging.getLogger(name)

    if isinstance(filelog_level, str):
        filelog_level = level_map(filelog_level)

    if isinstance(consolelog_level, str):
        consolelog_level = level_map(consolelog_level)

    logger.setLevel(logging.DEBUG)

    if not logger.handlers:

        # sets formatters
        filelog_formatter = logging.Formatter(format, datefmt=datefmt)
        consolelog_formatter = logging.Formatter(format, datefmt=datefmt)

        if filelog_format is not None:
            filelog_formatter = logging.Formatter(filelog_format, datefmt=datefmt)

        if consolelog_format is not None:
            consolelog_formatter = logging.Formatter(consolelog_format, datefmt=datefmt)

        # sets log level for logging to file
        if filelog_level is not None:
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(filelog_level)
            file_handler.setFormatter(filelog_formatter)
            logger.addHandler(file_handler)

        # sets log level for logging to console
        if consolelog_level is not None:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(consolelog_level)
            console_handler.setFormatter(consolelog_formatter)
            logger.addHandler(console_handler)

    return logger
