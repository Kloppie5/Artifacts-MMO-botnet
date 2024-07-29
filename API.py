import base64
import requests

API_ROOT = "https://api.artifactsmmo.com"

def GetRequest ( url, headers ) :
    response = requests.get(
        url=url,
        headers=headers
    )
    return response.json()
def PostRequest ( url, headers ) :
    response = requests.post(
        url=url,
        headers=headers
    )
    return response.json()

def GetStatus ( ) :
    return GetRequest(f"{API_ROOT}/")

def GenerateToken ( username, password ) :
    auth = base64.b64encode(f"{username}:{password}".encode()).decode()
    return PostRequest(f"{API_ROOT}/token/", {
        "Accept": "application/json",
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json"
    })["token"]