import json
import requests
import re
import os

def image_of(role_id):
    t = requests.get(f"https://wiki.bloodontheclocktower.com/File:Icon_{role_id}.png").text
    r = re.search(r'<a href="(.+?)" class="internal"', t)[1]
    return "https://wiki.bloodontheclocktower.com" + r

with open("../roles.json") as f:
    roles = json.load(f)
for role in roles:
    path = f"{role["id"]}.png"
    if os.path.exists(path): continue
    print(path)
    r = requests.get(image_of(role["id"])).content
    with open(path, "wb") as f:
        f.write(r)
