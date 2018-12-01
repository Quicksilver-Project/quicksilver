# UML reference database schema
# Copyright 2018 (C) Logan Campos - @binaryflesh
#
# imports
import os
import sys
import requests

run_Path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(run_Path, ".."))

from lib.config import Configuration

UML_BASE_URL = Configuration().getUMLBaseUrl()
UML_VERSION = Configuration().getUMLVersion()
UML_SOURCES = Configuration().parseUMLdataset()["UML"]

class Setup(Configuration):


    def __init__(self):
        self.conf = Configuration()
        self.version = self.conf.getUMLVersion()
        self.dataset = self.conf.parseUMLdataset()["UML"]["data"][self.version]
        self.urls = []
        self.buildUrls(self.dataset)
        #self.test()
        self.downloadDatafiles(urls=self.urls)

    def test(self) -> str:
        for i, e in enumerate(self.urls):
            print(e)

    def buildUrls(self, data) -> list:
        url = self.conf.getUMLBaseUrl()
        for key, value in data.items():
            url += f"/{key}"
            for k, v in value.items():
                _filename = ""#k
                if v == None:
                    _filename = v
                if isinstance(v, list):
                    if len(v["filename"]) > 1:
                        for index, element in enumerate(v["filename"]):
                            _filename += f"{element}"
                            self.urls.append(f"{url}/{_filename}")
                            _filename = ""#k
                elif isinstance(v, dict):
                    _filename += f"{v['filename'][0]}"
                    self.urls.append(f"{url}/{_filename}")

    def downloadDatafiles(self, urls=list) -> str:
        print(f"[*] Checking for UML {self.version} data sources...")
        for _, path in enumerate(urls):
            _filename = path.split("/")[-1:]
            if not os.path.exists(f"../data/UML/{self.version}/{_filename[0]}"):
                #TODO: Async progress bar
                print(f"[*] Downloading {_filename[0]} ...")
                r = requests.get(path, verify=False, allow_redirects=True)
                print(path)
                open(f"../data/UML/{self.version}/{_filename[0]}", "wb").write(r.content)
                print(f"[+] {_filename[0]} saved in quicksilver/data. ")
        print(f"[+] All data sources locally accessable.")



# "UML"-> "$version" -> "$uri" -> {["$filename"], ["$description"]}

if __name__ == "__main__":
    Setup()