#!/usr/bin/python33

import os
import configparser
import pickle
import json
import pkgutil
import re
import ast
import os
## cfg_file = pkgutil.get_data(__package__, 'application.conf')

configdata = ""

def read_config():
 #   cfg_file = pkgutil.get_data(__package__, 'application.conf')
    cfg_file = "application.conf"      #cfg = str(cfg)
    print("CFG")
    with open(cfg_file, "r") as f:
        data = f.read()
    exec(data)
    global configdata
    ast.literal_eval(configdata)
    #print(app_data)
    #cfg = json.loads(app_data)
    print(configdata)
    return configdata


cfg = read_config()

def write_complete_config(data):
    conf_file = "application.conf"
    data.encode('utf-8')
    with open(conf_file, 'w') as outfile:
        outfile.write("configdata=%s" % data)
    return data

cfg = read_config()

def get_cfg():
    return cfg
