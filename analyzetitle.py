import re
import subprocess
import os.path
import json

from config import cfg
#print(cfg['mediadirs']['Downloads'])
testmode = True

filedata = {}

def analyze(lines, orig_entry):
    # #print(lines)

    #print("> Data obtained. Analyzing...")
    #print()

    linedata = {}

    episodes = {}
    episode_counter = 1
    episode_names = []
    variants = {}
    opts = ""

    for line in lines:

        testmode = False

        if testmode:
            #logger.debug(line)
            print(line)

        # filebot line contains reference to TV show name auto-detection
        if re.search("Auto-detect", line):
            showname = re.search('.*\[(.*)\]', line)
            showname = showname.group(1)
            linedata['type'] = "tv"
            if re.search(".*\.srt", showname):
                linedata['srtfile'] = showname
            else:
                linedata['auto'] = showname

        # filebot line contains reference to movie title matching
        if line[0:8] == "Fetching":
            lineparts = line.split(" [")
            titlepart = lineparts[1]
            title = titlepart[:-2]
            linedata['title'] = title
            if re.search(".*\.srt", title):
                linedata['srtfile'] = title
            else:
                linedata['fetch'] = title

        # filebot line with "rename" also shows which database is being used
        if line[0:6] == "Rename":
            db = re.search('.*\[(.*)\]', line)
            db = db.group(1)
            if db == "TheTVDB":
                type = "tv"
                linedata['type'] = "tv"
            elif db == "TheMovieDB":
                type = "movie"
                linedata['type'] = "movie"
            else:
                type = "other"

            linedata['type'] = type

        # filebot line showing whether or not a file is renamed
        if (re.search("\[MOVE\]", line)) or (re.search("Skipped", line)):
            filename = ""
            filepath = ""

            # not renamed; filename is already correct
            if re.search("Skipped", line):
                grp1 = re.search('\[(.*)\].because.*$', line)
                match = grp1.group(1)
                filename = os.path.basename(match)
                filepath = os.path.dirname(match)
                episode_names.append(filename)

                # file needs renaming
            elif re.search("MOVE", line):
                findit = re.search('.*to \[(.*)\]', line)
                grp1 = findit.group(1)
                fullpath = grp1
                filename = os.path.basename(grp1)
                filepath = os.path.dirname(grp1)
                episode_names.append(filename)

            # both halves of above if/else set the same variables
            linedata['path'] = filepath
            if re.search(".*\.srt", filename):
                linedata['srtfile'] = filename
            else:
                linedata['moveskip'] = filename

        # ambigous tv show title; options shown and captured
        if line[0:8] == "Multiple":
            choices = re.search('.*\[(.*)\].*', line)
            opts = choices.group(1)
            opts = opts.split(", ")
            linedata['type'] = "multi"
            type = "multi"

    # -------- LINE() loop ends here ---------------#

    # assign parsed bits appropriate for TV show
    if linedata['type'] == "tv":
        filedata['type'] = "tv"
        filedata['episodes'] = []
        for ep in episode_names:
            parts = os.path.splitext(ep)
            if parts[1] != ".nfo":
                filedata['episodes'].append(ep)

        try:
            filedata['title'] = linedata['fetch']
        except KeyError:
            filedata['title'] = linedata['auto']
        filedata['path'] = linedata['path']

    # assign parsed data for movie entry
    if type == "movie":
        filedata['type'] = "movie"
        filedata['path'] = linedata['path']
        filedata['title'] = linedata['moveskip']

    elif type == "multi":
        filedata['title'] = linedata['auto']
        filedata['opts'] = opts

    else:
        print("tv filedata = ")
        print(filedata)
        return filedata

    print("filedata = ")
    print(filedata)
    return filedata

#def sendquery(verb, parm1, q=""):
def sendquery(parm1="", q=""):
    verb = "-rename"
    lines = []
    filedata = []
    print("PPP")
    print(parm1)
    print("PPP")
    orig_entry = parm1
    dldir = cfg['mediadirs']['Downloads']
    #print("DDD")
   # print(dldir)
    parm1 = os.path.join(dldir,parm1)

   # print("isdir")
   # print(os.path.isdir(dldir))
   # print("isfile")
   # print(os.path.isfile(dldir))

    if q == "":
        # the main machine - calls filebot with passed parameters
        #logger.info('QUERY SENT: %s' % dirName)
        #logger.info("\t%s" % parm1)




        proc = subprocess.Popen(["/snap/bin/filebot", verb, parm1, q], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:

        lines = []
        parm2 = "--q \"%s\"" % q

        #logger.info('QUERY SENT (extra param: %s) : %s' % (q, dirName))
        proc = subprocess.Popen(["filebot", verb, parm1, parm2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    for line in proc.stdout.readlines():
        # query each line and add to lines[] array
        line = line.decode(encoding="utf-8")
        lines.append(line)

    for line in proc.stderr.readlines():
        # query each line and add to lines[] array
        line = line.decode(encoding="utf-8")
        lines.append(line)

    # done, pass the array back
    #print(line)
    filedata = analyze(lines, orig_entry)
    filedata['original'] = orig_entry

    #print("os.path")
    #print(parm1)
    #print(os.path.isdir(parm1))
    #print(os.path.isfile(parm1))

    if os.path.isdir(parm1) == True:
        filedata['filefolder'] = "folder"
    if os.path.isfile(parm1) == True:
        filedata['filefolder'] = "file"

    fd_json = json.dumps(filedata)
    #print(fd_json)
    return fd_json
