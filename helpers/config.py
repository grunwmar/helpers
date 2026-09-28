import os
import sys
from helpers.xlogging import setup_logger
from helpers.load_config import load_config

CONFIGFILE = "./config/config.toml"

config = None

# if CONFIGFILE exists, loads it as dict to config variable
if os.path.isfile(CONFIGFILE):
    config = load_config(filename=CONFIGFILE, sysenv_subst=True, dotdict=True)
    log_config = config["log_config"]

    # if log_config file exists, loads it as dict to log_config variable
    # then initializes logger
    if os.path.isfile(log_config):
        logconfig = load_config(filename=log_config, sysenv_subst=True, dotdict=True)
        logger_name = logconfig.get("logger_name")
        logger = setup_logger(
            "logger" if logger_name is None else logger_name,
            datefmt=logconfig["date_format"],
            log_file=logconfig["file_log"]["filename"],
            filelog_level=logconfig["file_log"]["level"],
            filelog_format=logconfig["file_log"]["format"],
            consolelog_level=logconfig["console_log"]["level"],
            consolelog_format=logconfig["console_log"]["format"],
        )
        if config is not None:
            config["_logging"] = logconfig
    else:
        logger = setup_logger(f"{sys.argv[0]}", log_file="./log.txt")
