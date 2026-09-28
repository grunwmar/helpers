Creates basic directory tree for project. Creates `.venv` virtual environment and executable `./run.sh` running `__main__.py` in
`.venv`. Adds `helpers` python package to the project.
### Directory tree
```
----project/
    |
    |--helpers/<helpers_stuffs>
    |
    |--tests/
    |--logs/
    |--config/
    |   |
    |   |--config.toml
    |   |--logging.toml
    |
    |--.venv/<venv_stuffs>
    |--.gitignore
    |--make_venv.sh (executable)
    |--requrements.txt
    |--run.sh (executable)
```
# Usage
In new empty project directory run following command
```sh
curl -fsSL https://raw.githubusercontent.com/grunwmar/helpers/refs/heads/main/make_project/make.sh | bash -s
```
or
```sh
curl -fsSL https://mg91.cz/sh/pymk | bash -s
```

# helpers
## helpers.colors
Simple text enhancement.
```python
from helpers.colors import Clrs

# Create instance of Clrs object to predefine text style to use it repeatedly
clrs_rby = Clrs(1, 31, 43)

# Print red bold text on yellow backgroud
print("Text to be styled to red/yellow and bold" | clrs_rb)

# Use predefined string constants to stylize text
print(f"{Clrs.BOLD + Clrs.FG_RED + Clrs.BG_YELLOW}"
      f"Text to be styled to red/yellow and bold{Clrs.RESET}"
)

# Use static method co create stylized text
print(f"{Clrs.list(1, 31, 43)}"f"Text to be styled to red/yellow and bold{Clrs.RESET}")
```

## helpers.load_config
Predefined loading of configuration data from JSON/TOML files.
```python
from helpers.load_config import load_config

config = load_config(
    "config.json",
    sysenv_subst=True,
    dotdict=False,
)
# sysenv_subst=True ==> all strings will be searched for sequence of
# ${VAR_NAME} and will be replaced by values of os.environ("VAR_NAME")
# if such exists.
# 
# dotdict=True ==> use dict() derived class with implemented dot operator
# to access its keys.
# 
# fileformat="json"/"toml" ==> if format of config data can't be determined
# from an extension, it can be specified directly.
```

## helpers.xlogging
Predefined logger.
```python
from helpers.xlogging import setup_logger, DEBUG, INFO

logger = setup_logger(
    "logger_name"
    datefmt="%Y/%m/%d   %H:%M:%S",
    format="%(asctime)s   %(levelname)-8s   %(name)s   %(message)s",
    log_file="log.txt",
    filelog_level=DEBUG,
    filelog_format="%(asctime)s   %(levelname)-8s   %(name)s   %(message)s",
    consolelog_level=INFO,
    consolelog_format="%(asctime)s   %(levelname)-8s   %(name)s   %(message)s",
)

# format ==> used if filelog_format and/or consolelog_format not specified
```

## helpers.config
Predefined configuration.
```python
# log to logger defined in ./config/logging.toml
from helpers.config import logger as log

# default configuration in ./config/config.toml
from helpers.config import config

```
