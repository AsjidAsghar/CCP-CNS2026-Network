import paramiko
import time
from datetime import datetime
import os

# 1. Define the target devices (IP addresses configured in Week 1)
routers = [
    {"hostname": "R1", "ip": "192.168.1.1"},
    {"hostname": "R2", "ip": "192.168.1.2"},
    {"hostname": "R3", "ip": "192.168.1.3"}
]

# 2. SSH Credentials (Configured exactly as in Week 2)
username = "admin"
password = "Admin123"

# 3. Get the current date for the backup file names (Format: YYYY-MM-DD)
current_date = datetime.now().strftime("%Y-%m-%d")

# Create a local folder to store the downloaded backups if it doesn't exist
if not os.path.exists("router_backups"):
    os.makedirs("router_backups")

print("Starting Network Backup Automation Process...")
print("-" * 50)

for router in routers:
    print(f"Connecting to {router['hostname']} ({router['ip']})...")
    
    # Initialize the Paramiko SSH Client
    ssh = paramiko.SSHClient()
    
    # Automatically accept the SSH keys without prompting the user
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the router with a 10-second timeout if it's down
        ssh.connect(router['ip'], username=username, password=password, timeout=10)
        print(f"✅ Successfully connected to {router['hostname']}")
        
        # Open an interactive terminal session
        channel = ssh.invoke_shell()
        time.sleep(1)
        
        # CRITICAL: Disable terminal pagination so the config prints completely without hitting "--More--"
        channel.send("terminal length 0\n")
        time.sleep(1)
        
        # Send the command to view the running configuration
        channel.send("show running-config\n")
        time.sleep(3) # Give the router 3 seconds to output everything
        
        # Read the text stream coming back from the router
        output = channel.recv(65535).decode('utf-8')
        
        # Define the exact file name required by the project spec (router_name_date.txt)
        filename = f"router_backups/{router['hostname']}_{current_date}.txt"
        
        # Save the running config data into the file
        with open(filename, "w") as file:
            file.write(output)
            
        print(f"💾 Configuration saved to: {filename}")
        
    except paramiko.AuthenticationException:
        print(f"❌ Error: Authentication failed for {router['hostname']}. Check username/password.")
    except Exception as e:
        # Gracefully handle down routers so the script keeps running for the others
        print(f"❌ Error: Unreachable node! Could not connect to {router['hostname']}. Reason: {e}")
        
    finally:
        # Always close the SSH session clean
        ssh.close()
        print("-" * 50)

print("Backup automation task completed.")