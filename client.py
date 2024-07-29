
import time
import json

from API import *

class Client :

    def __init__ ( self, configfile ) :
        self.configfile = configfile
        with open(configfile) as f :
            data = json.load(f)
        self.token = GenerateToken(data["username"], data["password"])
        self.auth = f"Bearer {self.token}"
        self.UpdateCharacters()
    
    def Gather ( self ) :
        for name in self.characters :
            ActionGathering(self.auth, name)
        time.sleep(26)

    def Move ( self, x, y ) :
        for name in self.characters :
            ActionMove(self.auth, name, x, y)
        time.sleep(26)

    def UpdateCharacters ( self ) :
        self.characters = GetMyCharacters(self.auth)

    def DumpInventoryToBank ( self ) :
        for name in self.characters :
            ActionDepositBank(self.auth, name, self.characters[name]["inventory_slot1"], self.characters[name]["inventory_slot1quantity"])
        time.sleep(26)
        for name in self.characters :
            ActionDepositBank(self.auth, name, self.characters[name]["inventory_slot2"], self.characters[name]["inventory_slot2quantity"])
        time.sleep(26)
        for name in self.characters :
            ActionDepositBank(self.auth, name, self.characters[name]["inventory_slot3"], self.characters[name]["inventory_slot3quantity"])
        time.sleep(26)

        raise NotImplementedError()