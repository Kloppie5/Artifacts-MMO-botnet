import time
from client import Client

client = Client("config.json")
print(client.characters)

i = 0
while True :
    i += 1
    print(f"Mining {i}")
    client.Gather()

    if i % 3 == 0 :
        print(f"Banking")
        client.Move(4, 1)
        client.DumpInventoryToBank()
        client.Move(2, 0)
