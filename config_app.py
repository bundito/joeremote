import os
import configparser
import pickle
import json

cfg_file = "joe_app.conf"
cfg = ""




def read_config():
    cfg_file = "joe_app.conf"
    with open(cfg_file, "r") as f:
        cfg = f.read()
        #cfg = str(cfg)
    return cfg


def write_complete_config(data):
    print("QQQ")
    print(data)
    print("QQQ")
    with open('joe_app.conf', 'w') as f:
        f.write(data)
    return data
cfg = read_config()
