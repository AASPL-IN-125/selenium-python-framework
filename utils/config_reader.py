import configparser
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "config.ini")

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

def get_config(section, key):
    return config.get(section, key)

def get_base_url():
    return get_config("DEFAULT", "base_url")
