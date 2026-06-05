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

print("Starting Week 4 Network Backup Automation & Optimization Engine...")
print("-" * 60)

for router in routers:
    print(f"Connecting to {router['hostname']} ({router['ip']})...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(router['ip'], username=username, password=password, timeout=10)
        print(f"✅ Secure SSH Channel Established to {router['hostname']}")
        
        channel = ssh.invoke_shell()
        time.sleep(1)
        
        channel.send("terminal length 0\n")
        time.sleep(1)
        
        channel.send("show running-config\n")
        
        print("📥 Streaming running-configuration into local buffer sockets...")
        time.sleep(3) 
        
        output = channel.recv(65535).decode('utf-8')
        
        filename = f"router_backups/{router['hostname']}_{current_date}.txt"
        
        with open(filename, "w") as backup_file:
            backup_file.write(output)
        print(f"💾 Backup saved successfully: {filename}")
        
    except Exception as e:
        print(f"❌ Connection error on node {router['hostname']}: {e}")
        
    finally:
        ssh.close()
        print("-" * 60)

print("Week 4 traffic optimization routine complete.")