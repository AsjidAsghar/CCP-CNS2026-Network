import paramiko
import time
from datetime import datetime
import os

routers = [
    {"hostname": "R1", "ip": "192.168.1.1"},
    {"hostname": "R2", "ip": "192.168.1.2"},
    {"hostname": "R3", "ip": "192.168.1.3"}
]

username = "admin"
password = "Admin123"

current_date = datetime.now().strftime("%Y-%m-%d")

if not os.path.exists("router_backups"):
    os.makedirs("router_backups")

print("Starting Week 3 Network Backup Automation Process...")
print("-" * 50)

for router in routers:
    print(f"Initializing Secure Tunnel Context for {router['hostname']} ({router['ip']})...")
    
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Context setup complete for {router['hostname']}. Closing link baseline safely.")
    ssh.close()

print("-" * 50)
print("Week 3 pipeline baseline successfully executed.")