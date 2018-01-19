import os
import config_app
from config_app import cfg as app_cfg
import config
from config import cfg as sys_cfg
import json

def get_dest(filedata):

    filedata = json.loads(filedata)
    app_config = json.loads(app_cfg)

    print(filedata)

    if filedata['type'] == "tv":
        destbase = sys_cfg['mediadirs']['TV']
        showname = filedata['title']
        checkdest = os.path.join(destbase, showname)
        if not os.path.exists(checkdest):
            os.mkdir(checkdest, mode=0o777)
        dest = checkdest

        if app_config['dummycopy'] == "true":
            dest = "/home/bundito/DownloadBackup"

        src = os.path.join(filedata['path'], filedata['episodes'][0])

        if filedata['filefolder'] == "folder":
            folder_del = filedata['path']
        else:
            folder_del = None

    return(src, dest, folder_del)
