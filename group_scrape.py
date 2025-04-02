import requests
import json

def get_group_members(group_id, output_file):
    url = f"https://groups.roblox.com/v1/groups/{group_id}/users?limit=100"
    members = []
    
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            break
        
        data = response.json()
        members.extend([user['user']['username'] for user in data.get('data', [])])
        
        next_page = data.get('nextPageCursor')
        if next_page:
            url = f"https://groups.roblox.com/v1/groups/{group_id}/users?limit=100&cursor={next_page}"
        else:
            url = None
    
    with open(output_file, "w", encoding="utf-8") as file:
        for member in members:
            file.write(member + "\n")
    
    print(f"Successfully saved {len(members)} members to {output_file}")

if __name__ == "__main__":
    group_id = input("⚠️ Enter the Roblox group ID: ")
    output_file = "roblox_group_members.txt"
    get_group_members(group_id, output_file)
