# Configparser to scan config files
# 
# Copyright (c) 2018 Logan Campos - @binaryflesh

# imports
import os
import sys
run_Path = os.path.dirname(os.path.realpath(__file__))

import configparser
import json
    
class Configuration():
    ConfigParser = configparser.ConfigParser()
    ConfigParser.read(os.path.join(run_Path, "../etc/config.ini"))
    default = {"UmlBaseUrl": "https://www.omg.org/spec/UML/", "UmlVersion": "2.5.1"}

    @classmethod
    def readSetting(cls, section, item, default):
        result = default
        try:
            if isinstance(default, bool):
                result = cls.ConfigParser.getboolean(section, item)
            elif isinstance(default, int):
                result = cls.ConfigParser.getint(section, item)
            else:
                result = cls.ConfigParser.get(section, item)
        except:
            pass
        finally:
            return result

    @classmethod
    def getUMLBaseUrl(cls) -> str:
        return cls.readSetting("UML", "baseUrl", cls.default["UmlBaseUrl"])
    
    @classmethod
    def getUMLVersion(cls) -> str:
        return cls.readSetting("UML", "version", cls.default["UmlVersion"])

    @classmethod
    def parseUMLdataset(cls) -> dict:
        data = None
        with open("../etc/uml_sources.json") as f:
            data = json.load(f)
            f.close()
        return data
