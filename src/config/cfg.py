from configparser import ConfigParser
from from_root import from_here

file = 'config.ini'
config = ConfigParser()
config.read(from_here(file))


def get_value(section, key):
    return config[section][key]
