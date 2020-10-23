"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

from webexteamssdk import WebexTeamsAPI
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

api = WebexTeamsAPI()

addresses = []

#asks user if they have an email address to enter, user must input yes or no
more = input("Do you have an email address to enter (y/n)? ")

#asks users to for email address to enter
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
#Asks user to input another address
#If the user has another email address, they enter it, if not the script ends and prints
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
#prints email addresses    
print(addresses)

token = "Bearer {MjQ0NmFjZGUtMjlmZi00MDIyLTg1MmYtODllMGE0MDJmYTEyODEwMzViNDQtOTU2_PF84_consumer}"

#Create a new room
cyo4_room = api.rooms.create('webexteamssdk cyo4')

#Add email addresses to room
for email in addresses:
   api.memberships.create(cyo4.id, personemail=email)
   
#Post a message
api.message.create(cyo4_room.id, text="Welcome!"


