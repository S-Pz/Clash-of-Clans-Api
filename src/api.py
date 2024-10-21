from dotenv import load_dotenv
from requests import post, get
from urllib.parse import quote

import os, base64, json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("ascii")

    auth_base64 = str(base64.b64encode(auth_bytes), "ascii")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token

def get_auth_header(token):
  return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name, track_name):
  
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)

    encoded_artist = quote(artist_name)
    encoded_track = quote(track_name) if track_name else ""

    query = f"?q=remaster{encoded_track}track{encoded_track}artist{encoded_artist}&type=album"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)

    #verifying if exist a artist whitch this name
    if(len(json_result) == 0):
        print("No artist with this name exits ....")
        return None

    return json_result

if __name__ =='__main__':

    token = get_token()

    result = search_for_artist(token, "Wiz khalifa",'')
    with open("Artist_wiz_khalifa.json", "w",encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    artist_id = result['items']["artists"]['id']
    print(artist_id)