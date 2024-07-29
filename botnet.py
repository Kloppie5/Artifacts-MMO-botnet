import json
import requests
from API import *

f = open('config.json')
data = json.load(f)

token = GenerateToken(data["username"], data["password"])

print(token)
