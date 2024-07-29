import base64
import json
import requests

API_ROOT = "https://api.artifactsmmo.com"

def GetRequest ( url, headers={}, auth="" ) :
    response = requests.get(
        url=url,
        headers={
            "Accept": "application/json",
            "Authorization": auth,
            "Content-Type": "application/json",
        }|headers
    )
    response = response.json()
    with open('debug/last_get_response.json', 'w') as f:
        json.dump(response, f, indent=4)
    return response
def PostRequest ( url, headers={}, data={}, auth="" ) :
    response = requests.post(
        url=url,
        headers={
            "Accept": "application/json",
            "Authorization": auth,
            "Content-Type": "application/json",
        }|headers,
        data=data
    )
    response = response.json()
    with open('debug/last_post_response.json', 'w') as f:
        json.dump(response, f, indent=4)
    return response



def GetStatus ( ) :
    return GetRequest(f"{API_ROOT}/")

def ActionMove ( auth, name, x, y ) :
    return PostRequest(
        f"{API_ROOT}/my/{name}/action/move", 
        data={
            "x": x,
            "y": y
        },
        auth=auth)
def ActionEquipItem ( ) :
    raise NotImplementedError()
def ActionUnequipItem ( ) :
    raise NotImplementedError()
def ActionFight ( ) :
    raise NotImplementedError()
def ActionGathering ( auth, name ) :
    return PostRequest(
        f"{API_ROOT}/my/{name}/action/gathering", 
        auth=auth)
def ActionCrafting ( ) :
    raise NotImplementedError()
def ActionDepositBank ( auth, name, code, quantity ) :
    return PostRequest(
        f"{API_ROOT}/my/{name}/action/bank/deposit", 
        data={
            "code": code,
            "quantity": quantity
        },
        auth=auth)
def ActionDepositBankGold ( ) :
    raise NotImplementedError()
def ActionRecycling ( ) :
    raise NotImplementedError()
def ActionWithdrawBank ( ) :
    raise NotImplementedError()
def ActionWithdrawBankGold ( ) :
    raise NotImplementedError()
def ActionGeBuyItem ( ) :
    raise NotImplementedError()
def ActionGeSellItem ( ) :
    raise NotImplementedError()
def ActionAcceptNewTask ( ) :
    raise NotImplementedError()
def ActionCompleteTask ( ) :
    raise NotImplementedError()
def ActionTaskExchange ( ) :
    raise NotImplementedError()
def ActionDeleteItem ( ) :
    raise NotImplementedError()
def GetCharacterLogs ( ) :
    raise NotImplementedError()
def GetAllCharactersLogs ( ) :
    raise NotImplementedError()
def GetMyCharacters ( auth ) :
    characters = {}
    for character in GetRequest(f"{API_ROOT}/my/characters/", auth=auth)["data"] :
        characters[character["name"]] = character
    return characters
def GetBankItems ( ) :
    raise NotImplementedError()
def GetBankGolds ( ) :
    raise NotImplementedError()
def ChangePassword ( ) :
    raise NotImplementedError()

def CreateCharacter ( ) :
    raise NotImplementedError()
def GetAllCharacters ( ) :
    return GetRequest(f"{API_ROOT}/characters/")
def GetCharacter ( ) :
    raise NotImplementedError()

def GetAllMaps ( ) :
    raise NotImplementedError()
def GetMap ( ) :
    raise NotImplementedError()

def GetAllItems ( ) :
    raise NotImplementedError()
def GetItem ( ) :
    raise NotImplementedError()

def GetAllMonsters ( ) :
    raise NotImplementedError()
def GetMonster ( ) :
    raise NotImplementedError()

def GetAllResources ( ) :
    raise NotImplementedError()
def GetResources ( ) :
    raise NotImplementedError()

def GetAllEvents ( ) :
    raise NotImplementedError()

def GetAllGeItems ( ) :
    raise NotImplementedError()
def GetGeItem ( ) :
    raise NotImplementedError()

def CreateAccount ( ) :
    raise NotImplementedError()

def GenerateToken ( username, password ) :
    auth = base64.b64encode(f"{username}:{password}".encode()).decode()
    return PostRequest(f"{API_ROOT}/token/", auth=f"Basic {auth}")["token"]