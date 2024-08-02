import time
from API import *

class Analyzer :

    def __init__ ( self, configfile ) :
        self.configfile = configfile
        with open(configfile) as f :
            data = json.load(f)
        self.token = GenerateToken(data["username"], data["password"])
        self.auth = f"Bearer {self.token}"

    def GatherGEData ( self ) :
        items = GetAllGeItems(1, 100)
        items2 = GetAllGeItems(2, 100)

        with open("data/prices.csv", "r") as f :
            lines = set(f.readlines())
            for item in items + items2 :
                line = f"{item['code']},{item['stock']},{item['sell_price']}\n"
                if line not in lines :
                    print(f"New record {item}")
                    lines.add(line)
        with open("data/prices.csv", "w") as f :
            f.writelines(lines)
        

print(f"Running Analyzer;")
analyzer = Analyzer("config.json")
i = 0
while True :
    i += 1
    print(f"> GE check {i}")
    analyzer.GatherGEData()
    time.sleep(10)
