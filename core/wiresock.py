import json
import os

CONFIG_FILE = "profiles.json"

def load_profiles():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return []

def save_profiles(profiles):
    with open(CONFIG_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

def add_profile(name, server_ip, server_port, server_privkey, client_privkey, server_pubkey, client_pubkey):
    profiles = load_profiles()
    profiles.append({
        "name": name,
        "server_ip": server_ip,
        "server_port": server_port,
        "server_private_key": server_privkey,
        "client_private_key": client_privkey,
        "server_public_key": server_pubkey,
        "client_public_key": client_pubkey
    })
    save_profiles(profiles)

def delete_profile(name):
    profiles = load_profiles()
    profiles = [p for p in profiles if p["name"] != name]
    save_profiles(profiles)
