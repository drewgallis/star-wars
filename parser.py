# parser.py
# Drew Gallis
import re
f = open('starwars.txt', 'r+')

lst = []
count = 1
for line in f.readlines():
	#print('this is the line: ' + line)
	if "<b>" in line:
		test = line.split('<b>')
		for val in test:
			val = val.strip()
		    	if val:
				lst.append("start-bolded:" + str(count) + ":" + val)
	elif "</b>" in line:
		test = line.split('</b>')
		for val in test:
			val = val.strip()
			if val:
				lst.append("end-bolded:" + str(count) + ":" + val)
	else:
		line = line.strip()
		if line:
				lst.append("reg-line:" + str(count) + ":" + line)
	count += 1
f.close()

for val in lst:
	if "reg-line" in val:
		continue
	if "end-bolded" in val:
		continue
	if "start-bolded" in val:
		val = val.split(':')
		print(val[1] + ":" + val[2])
