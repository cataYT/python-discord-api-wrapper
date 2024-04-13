import requests
import json

BOT_TOKEN = "TOKEN_HERE"

def send_message(message, channelID=1098207196505968690, auth=BOT_TOKEN):
    url = f"https://discord.com/api/v9/channels/{channelID}/messages"
    body = {   
        "content": message,
        "tts": False, # text to speech
    }
    headers = {
        "Authorization": auth
    }
    result = requests.post(url, json=body, headers=headers).content.decode("utf-8")
    return json.loads(result)

def delete_message(messageID, channelID=1098207196505968690, auth=BOT_TOKEN):
    url = f"https://discord.com/api/v9/channels/{channelID}/messages/{messageID}"
    headers = {
        "authorization": auth,
    }
    return requests.delete(url=url, headers=headers)

def get_user_info(userID=925772708883615754, serverID=1119538529450594314, auth=BOT_TOKEN): # bot cannot do this
    url = f"https://discord.com/api/v9/users/{userID}/profile?with_mutual_guilds=true&with_mutual_friends=false&with_mutual_friends_count=false&guild_id={serverID}"
    headers = {
        "authorization": auth,
    }
    result = requests.get(url=url, headers=headers).content.decode("utf-8")
    return json.loads(result)

def login(token=BOT_TOKEN):
    url = 'https://discord.com/api/v9/auth/login'
    headers = {
        'Authorization': token
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        # Login successful
        data = response.json()
        return "login successful"
    else:
        # Login failed
        print(f'Failed to log in: {response.status_code} - {response.text}')
        return None
    
def create_channel(name, serverID, parentID=None, auth=BOT_TOKEN):
    url = f"https://discord.com/api/v9/guilds/{serverID}/channels"
    headers = {
        "authorization": auth,
        "content-type": "application/json"
    }
    body = {
        "type": 0,
        "name": name,
        "permission_overwrites": [],
        "parent_id": parentID
    }
    result = requests.post(url=url, json=body, headers=headers).content.decode("utf-8")
    return json.loads(result)

def delete_channel(channelID, auth=BOT_TOKEN):
    url = f"https://discord.com/api/v9/channels/{channelID}"
    headers = {
        "authorization": auth
    }
    result = requests.delete(url=url, headers=headers).content.decode("utf-8")
    return json.loads(result)

def update_roles(roles, userID, serverID, auth=BOT_TOKEN):
    url = f"https://discord.com/api/v9/guilds/{serverID}/members/{userID}"
    header = {
        "authorization": auth
    }
    body = {
        "roles": roles
    }
    result = requests.patch(url=url, headers=header, json=body).content.decode("utf-8")
    return json.loads(result)