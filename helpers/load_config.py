import os
from typing import Any


class _DotDict(dict):
    """
    a dictionary that supports dot notation
    as well as dictionary access notation
    usage: d = DotDict() or d = DotDict({'val1':'first'})
    set attributes: d.val2 = 'second' or d['val2'] = 'second'
    get attributes: d.val2 or d['val2']

    source: https://stackoverflow.com/questions/13520421/recursive-dotdict
    """

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        for key, value in dct.items():
            if hasattr(value, "keys"):
                value = _DotDict(value)
            self[key] = value


def _sysenv_subst(obj, parent: tuple) -> Any:
    """Substitutes $VARIABLE for os.path.environ["VARIABLE"] value"""

    if isinstance(obj, (list, tuple)):
        for index, item in enumerate(obj):
            _sysenv_subst(item, parent=(obj, index))

    elif isinstance(obj, dict):
        for key, item in obj.items():
            _sysenv_subst(item, parent=(obj, key))

    else:
        if isinstance(obj, str):
            for var, val in os.environ.items():
                obj = obj.replace(f"${var}", val)
            parent[0][parent[1]] = obj
        else:
            parent[0][parent[1]] = obj

    return obj


def _load_json(filename: str, sysenv_subst: bool = False) -> dict:
    """Loads JSON file and applies _sysenv_subst if required."""

    import json

    with open(filename, "r") as fp:
        data = json.load(fp)
        if sysenv_subst:
            return _sysenv_subst(data, ())
        return data


def _load_toml(filename: str, sysenv_subst: bool = False) -> dict:
    """Loads TOML file and applies _sysenv_subst if required."""

    import tomllib

    with open(filename, "rb") as fp:
        data = tomllib.load(fp)
        if sysenv_subst:
            return _sysenv_subst(data, ())
        return data


def load_config(filename, sysenv_subst=False, dotdict=False, fileformat=None):
    """Loads config file."""

    _, ext = os.path.splitext(filename)

    loaders = {
        ".json": _load_json,
        ".toml": _load_toml,
    }

    if fileformat is None:
        config = loaders[ext.lower()](filename, sysenv_subst)
    else:
        config = loaders[f".{fileformat.lower()}"](filename, sysenv_subst)

    if dotdict:
        return _DotDict(config)

    return config
