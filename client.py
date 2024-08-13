
import time
import json

from API import *

def main () :
    print(f"Client v2408011845")
    client = Client()
    i = 0
    client.Move(1, 6, 30)
    while True :
        i += 1
        print(f"Step {i}")
        client.Gather()

        if i % 90 == 1 :
            client.Move(4, 1, 35)
            client.UpdateCharacters()
            client.DumpInventoryToBank()
            client.Move(1, 6, 30)

# mining
# 2,0 copper (1)
# 1,7 iron (10)
# 1,6 coal (20)
# 10,-4 gold ore (30)

# woodcutting
# -1,0 ash (1) 
# 6,1 ash (1)
# -2,5 spruce (10)
# 2,6 spruce (10)
# 3,5 birch (20)
# -1,6 birch (20)
# 9,8 dead tree (30)

# fishing
# 4,2 gudgeon (1) 
# 5,2 shrimp (10)
# -3,6 bass (30)
# -2,6 trout (20)

# -5,-5 ogre
# -5,-4 ogre 
# -3,-3 pig 
# -2,-3 workshop woodcutting
# 0,-2 blue slime 
# 1,-2 yellow slime 
# 2,-2 red slime 
# 3,-2 green slime
# 0,-1 green slime 
# 1,-1 red slime 
# 2,-1 blue slime 
# 4,-1 yellow slime
# -3,0 wolf 
# -2,1 wolf 
# 0,1 chicken 
# 1,1 cooking 
# 2,1 weaponcrafting 
# 3,1 gearcrafting 
# 4,1 bank 
# 5,1 grand exchange
# 10,1 owlbear
# 0,2 cow 
# 1,2 task master 
# 10,2 owlbear
# 1,3 jewelrycrafting
# 5,3 mushmush
# 5,4 flying serpent
# 6,4 mushmush
# 1,5 mining
# 5,6 flying serpent
# 8,6 skeleton
# 10,6 vampire
# 8,7 death knight
# 9,7 lich
# 10,7 death knight
# 8,8 skeleton
# 10,8 vampire

class Client :

    def __init__ ( self ) :
        self.configfile = configfile
        self.auth = f"Bearer {self.token}"
        self.UpdateCharacters()
    
    # def GoToTaskMaster
    # 1,2 task master 

    def Gather ( self ) :
        print(f"Gathering")
        for name in self.characters :
            ActionGathering(self.auth, name)
        time.sleep(26)

    def Move ( self, x, y, sleep ) :
        print(f"Moving to {x}, {y}")
        for name in self.characters :
            ActionMove(self.auth, name, x, y)
        time.sleep(sleep+1)

    def UpdateCharacters ( self ) :
        print(f"Updating Characters")
        self.characters = GetMyCharacters(self.auth)

    def DumpInventoryToBank ( self ) :
        print(f"Dumping slot 1")
        for name in self.characters :
            ActionDepositBank(self.auth, name, self.characters[name]["inventory"][0]["code"], self.characters[name]["inventory"][0]["quantity"])
        time.sleep(4)

if __name__ == "__main__" :
    main()