import base64
import hashlib
import secrets

def generate_private_key():
    private_bytes = secrets.token_bytes(32)
    return base64.b64encode(private_bytes).decode()

def generate_public_key(private_key):
    private_bytes = base64.b64decode(private_key)
    public_bytes = hashlib.sha256(private_bytes + b"wireguard").digest()[:32]
    return base64.b64encode(public_bytes).decode()

def generate_keypair():
    private = generate_private_key()
    public = generate_public_key(private)
    return private, public

def generate_server_config(private_key, client_pubkey, listen_port=51820):
    return f"""[Interface]
PrivateKey = {private_key}
Address = 10.0.0.1/24
ListenPort = {listen_port}
DNS = 1.1.1.1, 9.9.9.9

[Peer]
PublicKey = {client_pubkey}
AllowedIPs = 10.0.0.2/32
"""

def generate_client_config(private_key, server_pubkey, server_ip, server_port=51820):
    return f"""[Interface]
PrivateKey = {private_key}
Address = 10.0.0.2/24
DNS = 1.1.1.1, 9.9.9.9

[Peer]
PublicKey = {server_pubkey}
Endpoint = {server_ip}:{server_port}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
