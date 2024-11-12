import os, requests, json

from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

def get_auth_header(token):
  
  return {
        "Accept":"application/json",
        "Authorization": "Bearer " + token
    }

def searh_for_player(token, player_tag):

    encoded_player_tag = quote(player_tag) if player_tag else ""

    url = "https://api.clashofclans.com/v1/players/" + encoded_player_tag
    header = get_auth_header(token)

    result = requests.get(url, headers=header)

    json_resul = json.loads(result.content)

    if(len(json_resul) == 0):
        print("No player founded")
        return None

    return json_resul

def search_for_clans(token, clan_tag):

    encoded_clan_tag = quote(clan_tag) if clan_tag else ""
    url = "https://api.clashofclans.com/v1/clans/" + encoded_clan_tag
    header = get_auth_header(token)

    result = requests.get(url, headers=header)

    json_resul = json.loads(result.content)

    if(len(json_resul) == 0):
        print("No clan founded")
        return None

    return json_resul

if __name__ == '__main__':

    player_tag = "#U8RRR8LY"
    clan_tag = "#2GCR8GL2P"

    # result = searh_for_player(API_TOKEN,player_tag)

    # with open(f"player{player_tag}Information.json","w", encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)

    result = search_for_clans(API_TOKEN, clan_tag)
    
    for a in result['memberList']:
        
        player_tag = a['tag']

        result = searh_for_player(API_TOKEN,player_tag)

        with open(f"player{player_tag}Information.json","w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

    with open(f"clan{clan_tag}Information.json","w", encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)