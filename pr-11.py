import socket
def dns_lookup():
   print("DNS Lookup Program")
   print("1. URL to IP Address")
   print("2. IP Address to URL")
   choice = input("Enter your choice (1 or 2): ")
   if choice == '1':
       # URL to IP Address Lookup
       url = input("Enter the URL (e.g., example.com): ")
       try:
           ip_address = socket.gethostbyname(url)
           print(f"The IP address of {url} is: {ip_address}")
       except socket.gaierror:
           print("Invalid URL or URL cannot be resolved.")
   elif choice == '2':
       # IP Address to URL Lookup
       ip_address = input("Enter the IP address (e.g., 93.184.216.34): ")
       try:
           url = socket.gethostbyaddr(ip_address)[0]
           print(f"The URL for IP address {ip_address} is: {url}")
       except socket.herror:
           print("Invalid IP address or IP cannot be resolved to a hostname.")
   else:
       print("Invalid choice. Please select 1 or 2.")
# Run the program
dns_lookup()


# Program Purpose

# To perform Domain Name System (DNS) Lookup —
# that means:

# Convert URL → IP address

# Convert IP address → URL

# 🧩 Example 1 – URL to IP Address
# ▶️ Input:
# DNS Lookup Program
# 1. URL to IP Address
# 2. IP Address to URL
# Enter your choice (1 or 2): 1
# Enter the URL (e.g., example.com): google.com

# 💻 Output:
# The IP address of google.com is: 142.250.193.206


# (IP address may differ depending on your network — it’s okay if you get a slightly different one.)

# 🧩 Example 2 – IP Address to URL
# ▶️ Input:
# DNS Lookup Program
# 1. URL to IP Address
# 2. IP Address to URL
# Enter your choice (1 or 2): 2
# Enter the IP address (e.g., 93.184.216.34): 142.250.193.206

# 💻 Output:
# The URL for IP address 142.250.193.206 is: maa03s62-in-f14.1e100.net

# ❌ Example of Invalid Input
# ▶️ Input:
# Enter your choice (1 or 2): 1
# Enter the URL (e.g., example.com): wrongurl.abc

# 💻 Output:
# Invalid URL or URL cannot be resolved.

# 🧾 Viva Explanation (Simple)

# socket.gethostbyname(url) → converts domain name to IP

# socket.gethostbyaddr(ip) → converts IP address to domain name

# Used in DNS servers to resolve website names

# Helpful in networking, browsers, and servers