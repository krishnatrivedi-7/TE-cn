import os

print("Remote DHCP Installation Simulator")
ip = input("Enter remote machine IP: ")
user = input("Enter username: ")
# In real use, we'd connect via SSH, but here we simulate
print(f"Connecting to {ip} as {user}...")

# Simulate installation command
print("Installing DHCP server on remote machine...")
os.system("echo 'sudo apt install isc-dhcp-server -y'")

print("DHCP server installed successfully (simulated).")


# Remote DHCP Installation Simulator
# Enter remote machine IP: 192.168.1.10
# Enter username: admin
# Connecting to 192.168.1.10 as admin...
# Installing DHCP server on remote machine...
# DHCP server installed successfully (simulated).
