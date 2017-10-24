#!/usr/bin/python
import random
import os
import string
import shelve
from os.path import expanduser
import argparse
import shutil

home = expanduser("~")
configPath = home+"/.config/"+"MakeItGreen/"
s = random.randrange(1,24)
working_dir = ""


def rand_string():
	tempr = random.randrange(1,125)
	rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(tempr))
	return rand

def make_changes():
	d = shelve.open(configPath+"Configuration")
	if "path" in d:
		path = d["path"]
		working_dir = path+"/"+d["link"].split("/")[4]+"/"
	print(working_dir)
	fname = rand_string()
	writing = open(working_dir+fname,'w+')
	temp = random.randrange(1,125)
	print(temp)
	for x in range(temp):
		writing.write(rand_string()+"\n")
	writing.close()
	os.system("cd "+working_dir+" && git add .")
	os.system("cd "+working_dir+" && git commit -m "+rand_string())
	d.close()


def setup_():
	configPath = home+"/.config/"+"MakeItGreen/"
	if not os.path.exists(configPath):
		os.mkdir(configPath)
	d = shelve.open(configPath+"Configuration")
	if results.SetupFlag:
		if "path" in d and "link" in d:
			path = d["path"]
			working_dir = path+"/"+d["link"].split("/")[4]+"/"
			if os.path.exists(working_dir):
				shutil.rmtree(working_dir)
			del d["path"]
			del d["link"]

	if "path" not in d:
		d["path"] = input("Enter path where you want to clone and make Misc Changes every time you run MakeItGreen:\n")
	if "link" not in d:
		d["link"] = input("Enter link to private repo for writing to remote:\n")
	if "path" in d and "link" in d:
		path = d["path"]
		working_dir = path+d["link"].split("/")[4]+"/"
		if not os.path.exists(working_dir):
			os.system("cd "+path+" && git clone "+d["link"])
	d.close()


parser = argparse.ArgumentParser()
parser.add_argument('--setup', action='store',
					dest='SetupFlag',
					help='Run --setup Y to re-setup',
			type=bool, default=False)
results = parser.parse_args()
if results.SetupFlag:
	setup_()

for x in range(s):
	make_changes()


d = shelve.open(configPath+"Configuration")
if "path" in d and "link" in d:
	path = d["path"]
	working_dir = path+"/"+d["link"].split("/")[4]+"/"
	if not os.path.exists(working_dir):
		os.system("cd "+path+" && git clone "+d["link"])
d.close()
print("current path:"+working_dir)
os.system("cd "+working_dir+" && git push")
