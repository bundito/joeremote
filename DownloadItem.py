import os.path


class DownloadItem:

    def __init__(self, path):

        self.dirname = os.path.dirname(path)
        self.filename = os.path.basename(path)
        self.fullpath = path
        self.type = ""
        self.title = ""
        self.episodes = ""
        self.destdir = ""


