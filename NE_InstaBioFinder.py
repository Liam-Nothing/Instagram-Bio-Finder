import instaloader

word_find = "NothingElse"
file_save = "username_verif.txt"
username = ""
password = ""
taget_username = "nothingelse.fr"
config_file = "config.txt"

def Load_cfg(config_file):
	global username, password
	with open(config_file) as file:
		lines = file.readlines()
		lines = [line.rstrip() for line in lines]
	username = lines[0]
	password = lines[1]

def Get_bio(username):
	L = instaloader.Instaloader()
	profile = instaloader.Profile.from_username(L.context, username)
	return profile.biography

def Test_bio(bio):
	if word_find in bio:
		return 1
	else:
		return 0

Load_cfg(config_file)
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
taget_username = input("> ")
print("==========================================================")
print("Please enter key word :")
word_find = input("> ")
print("==========================================================")
print("Loading of followers, please wait...")
print("==========================================================")
L = instaloader.Instaloader()
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, taget_username)

follow_list = []
count = 0
for followee in profile.get_followers():
	follow_list.append(followee.username)
	if(Test_bio(Get_bio(follow_list[count]))):
		f = open(file_save, "a")
		f.write(follow_list[count]+"\n")
		f.close()
		print("YES : " + follow_list[count])
	else:
		print("NO : " + follow_list[count])
	count = count + 1

print("==========================================================")
print("Press any key to close...")
print("All usernames that were found were added to the " + file_save)
print("==========================================================")
input('')