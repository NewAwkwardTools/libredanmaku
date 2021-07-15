from flask import Flask
import os
import toml

class Appearance:
    def ShowLogo(self,config):
        print(config['Appearance']['logo'])
class Initialization:
    def LoadConfig(self,filename):
        print("Loading Config")
        out = toml.load(filename)
        return out