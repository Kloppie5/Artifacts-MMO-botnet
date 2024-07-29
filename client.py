
import json

from API import *

class Client :

    def __init__ ( self, configfile ) :
        self.configfile = configfile
        with open(configfile) as f :
            data = json.load(f)
        self.token = GenerateToken(data["username"], data["password"])
    