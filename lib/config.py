# Configparser to scan config files
# 
# Copyright (c) 2018 Logan Campos - @binaryflesh

# imports
import os
import sys
run_Path = os.path.dirname(os.path.realpath(__file__))

import json
    
class Configuration():
    default = {
                "UmlBaseUrl": "https://www.omg.org/spec/UML/",
                "UmlVersion": "2.5.1",
                "XmiBaseUrl": "https://www.omg.org/spec/XMI/",
                "XmiVersion": "2.5.1",
    }

    #TODO: make self-contained tool to manage Modeling components.

    @classmethod
    def getUMLBaseUrl(cls) -> str:
        return cls.readSetting("UML", "baseUrl", cls.default["UmlBaseUrl"])
    
    @classmethod
    def getUMLVersion(cls) -> str:
        return cls.readSetting("UML", "version", cls.default["UmlVersion"])

    @classmethod
    def getUMLDataset(cls) -> dict:
        data = None
        with open("../etc/uml_sources.json") as f:
            data = json.load(f)
            f.close()
        return data
    
    @classmethod
    def getXMIBaseUrl(cls) -> str:
        return cls.readSetting("XMI", "baseUrl", cls.default["XmiBaseUrl"])
    
    @classmethod
    def getXMIVersion(cls) -> str:
        return cls.readSetting("XMI", "version", cls.default["XmiVersion"])
    
    @classmethod
    def getXMIDataset(cls) -> dict:
        data = None
        with open("../etc/xmi_sources.json") as f:
            data = json.load(f)
            f.close()
        return data
