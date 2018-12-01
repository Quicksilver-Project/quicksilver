# Modeling specification data source tool
# Copyright 2018 (C) Logan Campos - @binaryflesh
#
# imports
import os
import sys
import requests
import urllib3

# Annoying warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# cheap way to get back to root.
#TODO: make this a python package

run_Path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(run_Path, ".."))

from lib.config import Configuration
CONF = Configuration()

class Setup():
    """
    Generic Setup routine for OMG specifications.
    """
    #TODO: click CLI application to handle this in a main() def.
    def __init__(self, specs=["UML", "XMI"]):
        # temporary. need to make a smart tool to manage this.
        self.urls = []
        for _, spec in enumerate(specs):
            if spec == "UML":
                self.version = CONF.getUMLVersion()
                self.baseUrl = CONF.getUMLBaseUrl()
                self.dataset = CONF.getUMLDataset()[spec]["data"][self.version]
                if self.Download_Source():
                    print(f"[+] {spec}-{self.version} has been successfully downloaded.")
            elif spec == "XMI":
                self.version = CONF.getXMIVersion()
                self.baseUrl = CONF.getXMIBaseUrl()
                self.dataset = CONF.getXMIDataset()[spec]["data"][self.version]
                if self.Download_Source():
                    print(f"[+] {spec}-{self.version} has been successfully downloaded.")

    def Download_Source(self) -> bool:
        try:
            url = self.baseUrl
            for key, value in self.dataset.items():
                url += f"/{key}" # /yyyymmdd (usually)
                for _key, _value in value.items():
                    # document does not have a filename. the yyyymmdd indication is the URI to the spec.
                    if _value == None:
                        _filename = _value
                    elif isinstance(_value, list):
                        # same document, multiple attachments
                        if len(_value["filename"]) > 1:
                            for artifact in v["filename"]:
                                self.urls.append(url+"/"+artifact)
                    elif isinstance(_value, dict):
                        #yyyymmdd/UML.xmi
                        _filename = _value["filename"][0]
                    self.urls.append(url+"/"+_filename)
        except Exception as err:
            print(err)
            return False
        finally:
            for path in self.urls:
                _filename = path.split("/")[-1:][0]
                print(_filename)
                if not os.path.exists(f"../data/{_filename}"):
                    print(f"[*] Downloading {_filename} ...")
                    #TODO: Async progress bar
                    r = requests.get(path, verify=False, allow_redirects=True)
                    open(f"../data/{_filename}", "wb").write(r.content)
                print(f"[+] {_filename} saved in quicksilver/data.")
            return True

if __name__ == "__main__":
    Setup()