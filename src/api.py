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

def search_for_player(token, player_tag):

    encoded_player_tag = quote(player_tag) if player_tag else ""

    url = "https://api.clashofclans.com/v1/players/" + encoded_player_tag
    header = get_auth_header(token)

    result = requests.get(url, headers=header)

    json_resul = json.loads(result.content)

    if(len(json_resul) == 0):
        print("No player found")
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

def search_for_clan_war_log(token, clan_tag):
    
    encoded_clan_tag = quote(clan_tag) if clan_tag else ""
    url = "https://api.clashofclans.com/v1/clans/" + encoded_clan_tag + "/warlog"
    header = get_auth_header(token)

    result = requests.get(url, headers=header)

    json_resul = json.loads(result.content)

    if(len(json_resul) == 0):
        print("No clan war founded")
        return None
    
    return json_resul

def information_about_war(token, war_tag):

    encoded_war_tag = quote(war_tag) if war_tag else ""
    url = "https://api.clashofclans.com/v1/clanwarleagues/wars/" + encoded_war_tag
    header = get_auth_header(token)

    result = requests.get(url, headers=header)

    json_result = json.loads(result.content)

    if(len(json,result) == 0):
        print("No clan warleague founded")
        return None

    return json_result

def information_about_currentwar_leaguegroup(token, clan_tag):

    encoded_clan_tag = quote(clan_tag) if clan_tag else ""
    url = "https://api.clashofclans.com/vi/clans/" + encoded_clan_tag + "/currentwar/leaguegroup"
    header = get_auth_header(token)

    result = requests.get(url, headers=header)

    json_result = json.loads(result.content)

    if(len(json,result) == 0):
        print("No current war founded")
        return None
    
    return json_result

def clan_currentwar(token, clan_tag):

    encoded_clan_tag = quote(clan_tag) if clan_tag else ""
    url = "https://api.clashofclans.com/vi/clans" + encoded_clan_tag + "/currentwar"
    hearder = get_auth_header(token)

    result = requests.get(url, headers=hearder)

    json_resul = json.loads(result.content)

    if(len(json, result) == 0):
        print("No current war founded")
        return None
    
    return json_resul

def clan_capitalraid(token, clan_tag):

    encoded_clan_tag = quote(clan_tag) if clan_tag else ""
    url = "https://api.clashofclans.com/vi/clans" + encoded_clan_tag + "/capitalraidseasons"
    header = get_auth_header(token)

    result = requests.get(url, headers=header)

    json_resul = json.loads(result.content)

    if(len(json, result) == 0):
        print("No clan season founded")
        return None
    
    return json_resul

def search_clan(token:str, name:str="", locationId:int=32000038, limit:int=500):

    if name == "":
        url = f"https://api.clashofclans.com/v1/clans?locationId={locationId}&limit={limit}"
    else:
        url = f"https://api.clashofclans.com/v1/clans?name={name}&locationId={locationId}&limit={limit}"

    header = get_auth_header(token)

    result = requests.get(url, headers=header)
    
    json_result = json.loads(result.content)

    if len(json_result) == 0:
        print("Not found")
        return None
    
    return json_result

def clans_member_list(token,  clan_tag):

    encoded_clan_tag = quote(clan_tag) if clan_tag else ""
    
    url = f'https://api.clashofclans.com/v1/clans/{encoded_clan_tag}/members'
    header = get_auth_header(token)

    result = requests.get(url, headers=header)
    json_resul = json.loads(result.content)

    if(len(json, result) == 0):
        print("No clan season founded")
        return None
    
    return json_resul

if __name__ == '__main__':

    # player_tag = "#U8RRR8LY"
    # clan_tag = "#2GCR8GL2P"
    # locationId = 32000038 #Br

    # # result = searh_for_player(API_TOKEN,player_tag)

    # # with open(f"player{player_tag}Information.json","w", encoding='utf-8') as f:
    # #     json.dump(result, f, ensure_ascii=False, indent=4)

    # with open(f"clan{clan_tag}Information.json","w", encoding='utf-8') as f:
    #     json.dump(result, f, ensure_ascii=False, indent=4)
    
    clans_info:list=[]
    player_info_list:list=[]

    clans = search_clan(API_TOKEN,limit=500)
    cont:int = 0

    for info in clans['items']:
        
        clans_data = {

            'tag': info['tag'],
            'name':info['name'],
            'location':info['location']['countryCode'],
            'clanLevel':info['clanLevel'],
            'warFrequency':info['warFrequency'],
            'warFrequency': info['warFrequency'],
            'warWinStreak': info['warWinStreak'],
            'warWins': info['warWins'],
            'members': info['members'],
        }
        clans_info.append(clans_data)

        clan_details = search_for_clans(API_TOKEN, clans_data['tag'])
        
        #clans_member = clans_member_list(API_TOKEN,clans_data['tag'])
        
        if 'memberList' in clan_details:
            #print(clan_details)
            for player in clan_details['memberList']:
                player_tag = player['tag']

                player_info = search_for_player(API_TOKEN, player_tag)
                cont+=1

                print(cont)
                
                if player_info and 'tag' in player_info:
                    player_data = {
                        'tag': player_info['tag'],
                        'name': player_info['name'],
                        'townHallLevel': player_info['townHallLevel'],
                        'warStars': player_info['warStars'],
                        'attackWins': player_info['attackWins'],
                        'defenseWins': player_info['defenseWins'],
                        'donations': player_info['donations'],
                        'donationsReceived': player_info['donationsReceived'],
                        'clan_tag': player_info['clan']['tag'],
                        'clan_name': player_info['clan']['name']
                    }
                    print(player_data)
                    player_info_list.append(player_data)
                else:
                    print("Incomplete player data or player not found:", player_info)
            
    with open("clans_info.json","w", encoding='utf-8') as f:
        json.dump(clans_info, f, ensure_ascii=False, indent=4)

    with open("players_info.json","w", encoding='utf-8') as f:
        json.dump(player_info_list, f, ensure_ascii=False, indent=4)