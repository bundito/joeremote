import os
import json

from DownloadItem import DownloadItem

Listing = []

def clear_dupes(list):
    workarray = []
    for item in list:
        if item not in workarray:
            workarray.append(item)
    return workarray


def find_entries():
    dirs = []

    videofiles = ['mp4', 'avi', 'mkv']

    from collections import defaultdict
    dir_dict = defaultdict(dict)
    dir_dict['']['readme.txt'] = 1

    counter = 0
    # Set the directory you want to start from
    rootDir = '/home/bundito/Downloads'
    roots = defaultdict(dict)
    roots[rootDir]['hello.jpg'] = 2

    valid_entries = []

    # Goes through every file of every subdirectory, in that order
    for dirName, subdirList, fileList in os.walk(rootDir):

        for filename in fileList:
            # print(filename)
            file_ext = filename[-3:]

            # even though we've been checking file names,
            # all we care about is the containing directoru,
            # as long as the files have a video file extension
            if file_ext in videofiles:
                valid_entries.append(dirName)

    # above loop adds an entry for every TV show episode
    # we're going to process the whole directory, so get rid of the duplicates
    valid_entries = clear_dupes(valid_entries)

    # outside of os.walk now, checking rootDir for solo files
    for filename in os.listdir(rootDir):
       # print(filename)
        filename_ext = filename[-3:]
        #   print(filename_ext)
        if filename_ext in videofiles:
            entry = os.path.join(rootDir, filename)
            valid_entries.append(entry)

    try:
        valid_entries.remove(rootDir)
    except ValueError:
        dirs = ""
    return valid_entries


#----------------- START -----------------------#


entries = find_entries()

for item in entries:
    #print(item)
    obj = DownloadItem(item)
    Listing.append(obj)

"""
jtemp = {}
jdata = {}
jinner = []
filename = ""
counter = 0
for item in Listing:
    print(filename)
    filename = item.filename
    jtemp['dir'] = filename
    jinner.append(jtemp)
    jtemp = {}
    counter += 1
#jdata.append(jinner)
jdata["dirlist"] = jinner
"""


jtemp = {}
jdata = {}
jinner = []
filename = ""
counter = 0
for item in Listing:
    #print(filename)
    filename = item.filename
    jinner.append(filename)

    jtemp = {}
    counter += 1
#jdata.append(jinner)
#jdata["dirlist"] = jinner

jaysun = json.dumps(jinner)

#def get_json():
#    return jaysun

def get_list():
    return jinner




