# 🔐 VPN Manager — WireGuard Key Generator & Connection Watchdog

A simple and powerful tool to generate WireGuard VPN keys, build server/client configs, save profiles, and monitor connection stability.

---

## 📋 Features

| Feature | Description |
|---------|-------------|
| 🔑 **Key Generator** | Generate WireGuard private and public keypairs |
| 📄 **Config Builder** | Create server and client configs automatically |
| 💾 **Profile Manager** | Save, load, and delete VPN profiles |
| 🛡 **Watchdog** | Monitor connection, auto-detect drops, restart if needed |
| 🎨 **Dark Theme** | Modern dark interface, easy to use |

---

## 🛠 How to Install

### Automatic (recommended)
1. Double-click `install.cmd`
2. It will download and install Python 3.14.2 automatically
3. Program starts right after installation

### Manual
1. Install Python 3.14.2 from [python.org](https://python.org)
2. Open CMD and type:
pip install pillow qrcode
python main.py

text

---

## 🚀 How to Use

### Generate Keys
1. Open **Keys** tab
2. Click **"Generate Keypair"**
3. Private and Public keys appear
4. Keep Private Key secret! Share Public Key with friends

### Build Configs
1. Open **Configs** tab
2. Enter your server IP address
3. Enter a profile name (example: "Home", "Office")
4. Click **"Generate Configs"**
5. Server and Client configs appear
6. Profile is saved automatically

### Use Watchdog
1. Open **Watchdog** tab
2. Click **"Start Watchdog"**
3. It pings `1.1.1.1` every 10 seconds
4. If connection drops — shows warning
5. Click again to stop

### Connect Devices
1. Copy the **Client Config** from Configs tab
2. Save it as `client.conf`
3. Import into WireGuard app on your phone/PC
4. Connect!

---

## 📁 Project Structure
VPN-Manager/
├── README.md ← this file
├── install.cmd ← one-click installer
├── main.py ← main application
└── core/
├── init.py ← module init
├── keygen.py ← key generator
├── wiresock.py ← profile manager
└── watchdog.py ← connection monitor

text

---

## 📊 How It Works
[Key Generator] → Private Key + Public Key
↓
[Config Builder] → Server Config + Client Config
↓
[Profile Manager] → Save / Load Profiles
↓
[Watchdog] → Ping 1.1.1.1 → Connection OK? → Yes: Keep monitoring
→ No: Show warning

text

---

## ❓ FAQ

**Q: Is it free?**  
A: Yes, completely free. Keys are generated locally on your PC.

**Q: Do I need a server?**  
A: Yes, you need a server with WireGuard installed. This tool generates configs for it.

**Q: Is my data safe?**  
A: Yes, all keys are stored locally in `profiles.json`. Nothing is sent anywhere.

**Q: Can I share my config with friends?**  
A: Yes! Share the **Client Config** with friends so they can connect to your server.

**Q: What if connection drops?**  
A: Watchdog detects it and shows a warning. You can restart the connection manually.

---

## 👤 Author

**Mark**, 10 years old

> Building tools to help the world. One project at a time. 🔥

---

## 📄 License

Free to use, modify, and share.
