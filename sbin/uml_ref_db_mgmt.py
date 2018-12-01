# UML reference database schema
# Copyright 2018 (C) Logan Campos - @binaryflesh
#
# imports
import os
import sys
import requests

# cheap way to get back to root.
#TODO: make this a python package

run_Path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(run_Path, ".."))

from lib.config import Configuration

class Setup(Configuration):
    """
    WIP:
    Will configure a sqlite3 reference table based on UML entity specs
    """
    def __init__(self):
        self.conf = Configuration()
        self.version = self.conf.getUMLVersion()
        self.dataset = self.conf.parseUMLdataset()["UML"]["data"][self.version]
        self.urls = []
        self.buildUrls(self.dataset)
        self.downloadDatafiles(urls=self.urls)

    def buildUrls(self, data) -> list:
        url = self.conf.getUMLBaseUrl()
        for key, value in data.items():
            url += f"/{key}" #/yyyymmdd
            for k, v in value.items():
                if v == None:
                    _filename = v #document does not have a filename. the URI is key
                if isinstance(v, list):
                    # same document, multiple attachments
                    if len(v["filename"]) > 1:
                        for index, element in enumerate(v["filename"]):
                            self.urls.append(f"{url}/{element}")
                elif isinstance(v, dict):
                    # /yyyymmdd/UML.xmi
                    _filename = f"{v['filename'][0]}"
                self.urls.append(f"{url}/{_filename}")

    def downloadDatafiles(self, urls=list) -> str:
        print(f"[*] Checking for UML {self.version} data sources...")
        for _, path in enumerate(urls):
            _filename = path.split("/")[-1:][0]
            if not os.path.exists(f"../data/UML/{self.version}/{_filename}"):
                print(f"[*] Downloading {_filename} ...")
                #TODO: Async progress bar
                r = requests.get(path, verify=False, allow_redirects=True)
                open(f"../data/UML/{self.version}/{_filename}", "wb").write(r.content)
                print(f"[+] {_filename} saved in quicksilver/data. ")
        print(f"[+] All data sources locally accessable.")

if __name__ == "__main__":
    Setup()