import random
import os
import string
import shelve
from os.path import expanduser
home = expanduser("~")
configPath = home+"/.config/"+"MakeItGreen/"
s = random.randrange(1,24)



def rand_string():
	tempr = random.randrange(1,125)
	rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(tempr))
	return rand

def make_changes():
	d = shelve.open(configPath+"Configuration")
	if "path" not in d:
		d["path"] = input("Enter path where you want to clone and make Misc Changes every time you run MakeItGreen:\n")
	elif "path" in d:
		path = d["path"]
	working_dir = path+d["link"].split("/")[4]+"/"
	print(working_dir)
	fname = rand_string()
	writing = open(working_dir+fname,'w+')
	temp = random.randrange(1,125)
	print(temp)
	for x in range(temp):
		writing.write(rand_string()+"\n")
	writing.close()
	os.system("git add .")
	os.system("git commit -m "+rand_string())


def setup_():
	configPath = home+"/.config/"+"MakeItGreen/"
	# os.system("cd "+"~/.config/ && pwd")
	# print(configPath)
	# os.system("")
	if not os.path.exists(configPath):
		os.mkdir(configPath)
	d = shelve.open(configPath+"Configuration")
	if "path" not in d:
		d["path"] = input("Enter path where you want to clone and make Misc Changes every time you run MakeItGreen:\n")
	# elif "path" in d:
		# print(d["path"])
	if "link" not in d:
		d["link"] = input("Enter link to private repo for writing to remote:\n")
	# elif "link" in d:
		# print(d["link"].split("/")[4])
	if "path" in d and "link" in d:
		path = d["path"]
		working_dir = path+d["link"].split("/")[4]+"/"
		if not os.path.exists(working_dir):
			print("not exists")
			os.system("cd "+path+" && git clone "+d["link"])
	d.close()

setup_()
# make_changes()

# link = input("Enter link to private repo for writing to remote:\n")

# path = input("Enter path where you want to clone and make Misc Changes every time you run MakeItGreen:\n")

# print(path)
# os.system("cd "+path +" && git clone "+link)

# os.system("git clone "+link)

# for x in range(s):
# 	make_changes()

# os.system("git log")
#print(s)
