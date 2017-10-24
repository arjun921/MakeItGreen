import random
import os
import string
s = random.randrange(1,24)



def rand_string():
	tempr = random.randrange(1,125)
	rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(tempr))
	return rand

def make_changes():
	fname = rand_string()
	writing = open(fname,'w+')
	temp = random.randrange(1,125)
	print(temp)
	for x in range(temp):
		writing.write(rand_string()+"\n")
	writing.close()
	os.system("git add .")
	os.system("git commit -m "+rand_string())

for x in range(s):
	make_changes()

os.system("git log")
#print(s)
