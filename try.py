import re

with open("pytotext.txt") as f:
	lines = f.readlines()

lineNumber = 0
for line in lines:
	if lineNumber < 10:
		if line.find('Mobile') >= 0:
			mob = line.split(':')[1]
			print(mob)
		if line.find('email') >= 0:
			email = line.split(':')[1]
			print(email)
	if line.find('Reference ') >= 0:
		print(lineNumber)
		
		name = re.split(': | \t', lines[lineNumber + 2])[1]
		organization = re.split(':', lines[lineNumber + 3])[1]
		designation = re.split(': | \t', lines[lineNumber + 4])[1]
		mobile = re.split(': | \t', lines[lineNumber + 8])[1]
#		email = re.split(': | \t', lines[lineNumber + 9])[1]
		print(re.split(r'\s{2,}', name))
		print(re.split(r'\s{2,}', organization))
		print(re.split(r'\s{2,}', designation))
		print(re.split(r'\s{2,}', mobile))
#		print(re.split(r'\s{2,}', email))
		print(lines[lineNumber + 2].split(":")[0])

	if line.find('Employment History') >= 0:
		job = lines[lineNumber + 2 : lineNumber + 6]
		print(job)
	
	lineNumber += 1


