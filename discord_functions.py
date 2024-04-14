import requests
import json
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = dotenv.dotenv_values(".env").get("BOT_TOKEN")

HEADERS = {
    "authorization": BOT_TOKEN
}

BASE_URL = "https://discord.com/api/v9"

def send_message(message, channelID=1098207196505968690):
    url = f"{BASE_URL}/channels/{channelID}/messages"
    body = {   
        "content": message,
    }
    result = requests.post(url, json=body, headers=HEADERS).content.decode("utf-8")
    return json.loads(result)

def delete_message(messageID, channelID=1098207196505968690):
    url = f"{BASE_URL}/channels/{channelID}/messages/{messageID}"
    return requests.delete(url=url, headers=HEADERS)

def get_user_info(userID=925772708883615754, serverID=1119538529450594314, auth=BOT_TOKEN): # bot cannot do this
    url = f"{BASE_URL}/users/{userID}/profile?with_mutual_guilds=true&with_mutual_friends=false&with_mutual_friends_count=false&guild_id={serverID}"
    result = requests.get(url=url, headers=HEADERS).content.decode("utf-8")
    return json.loads(result)

def login(token=BOT_TOKEN):
    url = f'{BASE_URL}/v9/auth/login'
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
    
def create_channel(name, serverID, parentID=None):
    url = f"{BASE_URL}/guilds/{serverID}/channels"
    headers = {
        "authorization": BOT_TOKEN,
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

def delete_channel(channelID):
    url = f"{BASE_URL}/channels/{channelID}"
    result = requests.delete(url=url, headers=HEADERS).content.decode("utf-8")
    return json.loads(result)

def update_roles(roles, userID, serverID):
    url = f"{BASE_URL}/guilds/{serverID}/members/{userID}"
    body = {
        "roles": roles
    }
    result = requests.patch(url=url, headers=HEADERS, json=body).content.decode("utf-8")
    return json.loads(result)

def get_members_info(serverID, limit=250):
    url = f"{BASE_URL}/guilds/{serverID}/members-search"
    body = {
        "or_query": {},
        "and_query": {},
        "limit": limit
    }
    result = requests.post(url=url, json=body, headers=HEADERS).content.decode("utf-8")
    return json.loads(result)

def pin_message(channelID, messageID):
    url = f"{BASE_URL}/channels/{channelID}/pins/{messageID}"
    result = requests.put(url=url, headers=HEADERS).content.decode("utf-8")
    return json.loads(result)

def unpin_message(channelID, messageID):
    url = f"{BASE_URL}/channels/{channelID}/pins/{messageID}"
    result = requests.delete(url=url, headers=HEADERS).content.decode("utf-8")
    return json.loads(result)

def get_pins(channelID):
    url = f"{BASE_URL}/channels/{channelID}/pins"
    result = requests.get(url=url, headers=HEADERS).content.decode("utf-8")
    return json.loads(result)

def crosspost_message(channel_id, message_id):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/crosspost'
    headers = {
        'Authorization': BOT_TOKEN,
        'Content-Type': 'application/json',
    }
    result = requests.post(url, headers=headers).content.decode("utf-8")
    return json.loads(result)