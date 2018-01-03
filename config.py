import os
import configparser
import pickle

cfg_file = "joe.conf"

config = configparser.ConfigParser()
config.read(cfg_file)

cfg = config

print("XXX")
print(cfg)
print("XXX")


def read_config():
    cfg_file = "joe.conf"

    config = configparser.ConfigParser()
    config.read(cfg_file)

    return config

def write_config(key, value):

    cfg_file = "joe.conf.old"
    cfg[key] = value

    with open(cfg_file, 'w') as configfile:
        configfile.write(cfg)
    configfile.close()

print
def write_complete_config(configdata):



    cfg_file = "joe.conf"

    print("QQQ")
    print(configdata)
    print("QQQ")

    with open(cfg_file, 'w') as configfile:
        configfile.write(configdata)


