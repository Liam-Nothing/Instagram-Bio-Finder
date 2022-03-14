from ast import Continue
import instaloader
import time
import random
import requests
import shutil
import os
import json
from os.path import exists

now = time.localtime(time.time())
config_file = "config.json"

def Progress(content):
	payload = {'api': 'update_content', 'label': json_config["api_label"], 'pass': json_config["api_password"], 'content': str(content)}
	rep = requests.get(json_config["api_url"], params=payload)

def Load_cfg(config_file):
	f = open(config_file)
	data = json.load(f)
	f.close()
	return data

def Get_bio(username):
	L = instaloader.Instaloader()
	profile = instaloader.Profile.from_username(L.context, username)
	return profile.biography

def Edit_compteur(compteur):
	f = open(target_username + "_compteur.txt", "w")
	f.write(compteur)
	f.close()

def Test_bio(bio):
	pause = random.uniform(1,2)
	time.sleep(pause)
	if word_find in bio:
		return 1
	else:
		return 0

print("==========================================================")
print("  _   _       _   _     _             ______ _          ")
print(" | \ | |     | | | |   (_)           |  ____| |         ")
print(" |  \| | ___ | |_| |__  _ _ __   __ _| |__  | |___  ___ ")
print(" | . ` |/ _ \\| __| '_ \\| | '_ \\ / _` |  __| | / __|/ _ \\")
print(" | |\  | (_) | |_| | | | | | | | (_| | |____| \__ \  __/")
print(" |_| \_|\___/ \__|_| |_|_|_| |_|\__, |______|_|___/\___|")
print("                                 __/ |                  ")
print("        NothingElse.fr          |___/                   ")
print("==========================================================")
print("[Python Script] Instagram bio finder.")
print("==========================================================")
print("[Goal] Enter a username and let the program see\n       if in followers of the username have\n       the key word in bio.")
print("==========================================================")
print("Please a username :")
target_username = input("> ")
print("==========================================================")
print("Please enter key word :")
word_find = input("> ")
print("==========================================================")
print("Loading of followers, please wait...")
print("==========================================================")
json_config = Load_cfg(config_file)
L = instaloader.Instaloader()
L.login(json_config["username"], json_config["password"])
profile = instaloader.Profile.from_username(L.context, target_username)

follow_list = []
count = 0
compteur = 0

if not exists(target_username + "_followers.json"):
	for followee in profile.get_followers():
		follow_list.append(followee.__dict__["_node"])
	f = open(target_username + "_followers.json", "w")
	f.write(json.dumps(follow_list, indent=4))
	f.close()

f = open(target_username + "_followers.json")
dict_followers = json.load(f)
f.close()

if exists(target_username + "_compteur.txt"):
	f = open(target_username + "_compteur.txt")
	start_id = json.load(f)
	compteur = start_id
	f.close()
else:
	start_id = 0

for id in range(start_id, len(dict_followers)):
	if (Test_bio(Get_bio(dict_followers[id]["username"]))):
		print([time.strftime("%d/%m/%y %H:%M", now)], "[" + str(compteur) + "]" + ": YES : " + dict_followers[id]["username"])
	else:
		print([time.strftime("%d/%m/%y %H:%M", now)], "[" + str(compteur) + "]" + ": NO : " + dict_followers[id]["username"])
	Progress(str(compteur))
	compteur += 1
	Edit_compteur(str(compteur))

print("==========================================================")
print("Press any key to close...")
print("All usernames that were found were added to the " + target_username + "_followers.json")
print("==========================================================")
input('')