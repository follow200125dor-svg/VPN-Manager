import tkinter as tk
from tkinter import ttk, messagebox
from core.keygen import generate_keypair, generate_server_config, generate_client_config
from core.wiresock import load_profiles, add_profile, delete_profile
from core.watchdog import Watchdog

root = tk.Tk()
root.title("VPN Manager")
root.geometry("800x700")
root.configure(bg="#1e1e2e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#1e1e2e")
style.configure("TLabel", background="#1e1e2e", foreground="#cdd6f4", font=("Arial", 11))
style.configure("TButton", background="#45475a", foreground="#cdd6f4", font=("Arial", 10, "bold"))
style.map("TButton", background=[("active", "#89b4fa")])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# ====== TAB 1: KEY GENERATOR ======
keys_frame = ttk.Frame(notebook)
notebook.add(keys_frame, text="🔑 Keys")

ttk.Label(keys_frame, text="WireGuard Key Generator", font=("Arial", 16, "bold"), foreground="#89b4fa").pack(pady=15)

ttk.Label(keys_frame, text="Private Key:").pack(anchor="w", padx=20)
private_entry = tk.Entry(keys_frame, bg="#313244", fg="#cdd6f4", font=("Consolas", 10), width=60, state="readonly")
private_entry.pack(padx=20, pady=5)

ttk.Label(keys_frame, text="Public Key:").pack(anchor="w", padx=20)
public_entry = tk.Entry(keys_frame, bg="#313244", fg="#cdd6f4", font=("Consolas", 10), width=60, state="readonly")
public_entry.pack(padx=20, pady=5)

def gen_keys():
    private, public = generate_keypair()
    private_entry.config(state="normal")
    private_entry.delete(0, tk.END)
    private_entry.insert(0, private)
    private_entry.config(state="readonly")
    public_entry.config(state="normal")
    public_entry.delete(0, tk.END)
    public_entry.insert(0, public)
    public_entry.config(state="readonly")

ttk.Button(keys_frame, text="Generate Keypair", command=gen_keys).pack(pady=15)

# ====== TAB 2: CONFIGS ======
config_frame = ttk.Frame(notebook)
notebook.add(config_frame, text="📄 Configs")

ttk.Label(config_frame, text="Generate VPN Configs", font=("Arial", 16, "bold"), foreground="#89b4fa").pack(pady=15)

ttk.Label(config_frame, text="Server IP:").pack(anchor="w", padx=20)
server_ip_entry = tk.Entry(config_frame, bg="#313244", fg="#cdd6f4", font=("Arial", 11), width=30)
server_ip_entry.pack(padx=20, pady=5)
server_ip_entry.insert(0, "123.456.789.0")

ttk.Label(config_frame, text="Profile Name:").pack(anchor="w", padx=20)
profile_name_entry = tk.Entry(config_frame, bg="#313244", fg="#cdd6f4", font=("Arial", 11), width=30)
profile_name_entry.pack(padx=20, pady=5)

config_display = tk.Text(config_frame, bg="#313244", fg="#cdd6f4", font=("Consolas", 9), height=20, state="disabled")
config_display.pack(fill="both", expand=True, padx=20, pady=10)

def gen_configs():
    server_priv, server_pub = generate_keypair()
    client_priv, client_pub = generate_keypair()
    server_ip = server_ip_entry.get()
    name = profile_name_entry.get() or "Default"
    
    server_cfg = generate_server_config(server_priv, client_pub)
    client_cfg = generate_client_config(client_priv, server_pub, server_ip)
    
    config_display.config(state="normal")
    config_display.delete("1.0", tk.END)
    config_display.insert("1.0", f"=== SERVER ===\n{server_cfg}\n=== CLIENT ===\n{client_cfg}")
    config_display.config(state="disabled")
    
    add_profile(name, server_ip, 51820, server_priv, client_priv, server_pub, client_pub)
    messagebox.showinfo("Saved", f"Profile '{name}' saved!")

ttk.Button(config_frame, text="Generate Configs", command=gen_configs).pack(pady=10)

# ====== TAB 3: WATCHDOG ======
watchdog_frame = ttk.Frame(notebook)
notebook.add(watchdog_frame, text="🛡 Watchdog")

ttk.Label(watchdog_frame, text="Connection Watchdog", font=("Arial", 16, "bold"), foreground="#89b4fa").pack(pady=15)

watchdog_status = ttk.Label(watchdog_frame, text="Status: Stopped", font=("Arial", 14), foreground="#f38ba8")
watchdog_status.pack(pady=10)

wd = Watchdog()

def toggle_watchdog():
    if wd.running:
        wd.stop()
        watchdog_status.config(text="Status: Stopped", foreground="#f38ba8")
        wd_btn.config(text="Start Watchdog")
    else:
        def on_disconnect():
            watchdog_status.config(text="Status: DISCONNECTED!", foreground="#fab387")
        wd.start(on_disconnect)
        watchdog_status.config(text="Status: Running", foreground="#a6e3a1")
        wd_btn.config(text="Stop Watchdog")

wd_btn = ttk.Button(watchdog_frame, text="Start Watchdog", command=toggle_watchdog)
wd_btn.pack(pady=20)

ttk.Label(watchdog_frame, text="Pings 1.1.1.1 every 10 seconds\nAuto-restarts if connection lost", font=("Arial", 9), foreground="#6c7086").pack(pady=10)

root.mainloop()
