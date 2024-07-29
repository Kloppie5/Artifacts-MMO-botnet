import requests

API_ROOT = "https://api.artifactsmmo.com/"

def GetStatus ( ) :
    return requests.get(
        url=API_ROOT
    ).json()
