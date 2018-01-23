'''
For windows. Tested on windows 10
- include poppler to windows path variable
- run python try-win.py pdf/1.pdf

'''

import math
import re
import sys
import subprocess

filename = sys.argv[1]

args = ['pdftotext', '-layout', '-q', filename, '-']
# args = ['pdftotext', '-layout', '-q', filename, '-']
doc = subprocess.check_output(args, universal_newlines=True)

print(doc)

lines = doc.split('\n')

lineNumber = 0

nameOne = lines[9].lstrip()
# print(nameOne)

reference = math.nan 

emailOne = ""
emailTwo = ""
emailThree = ""

for line in lines:
	if lineNumber < 30:
		if line.find('Mobile') >= 0:
			mobOne = line.split(':')[1].lstrip()
			# print(mobOne)
		if line.find('email') >= 0:
			emailOne = line.split(':')[1].lstrip()
			# print(emailOne)
	if line.find('Reference ') >= 0:
		reference = lineNumber
	
	if lineNumber > reference:
		try:
			if line.find('Mobile') >= 0:
				mobile = re.split(':', line)[1].lstrip()
				mobile = re.split('\s{2,}', mobile)
				mobTwo = mobile[0]
				mobThree = mobile[1]
				# print(mobTwo)
				# print(mobThree)

			elif line.find('EMail') >= 0:
				email = re.split(':', line)[1].lstrip()
				email = re.split('\s{2,}', email)
				emailTwo = email[0]
				emailThree = email[1]
				# print(emailTwo)
				# print(emailThree)
			
			elif line.find('Organization') >= 0:
				organization = re.split(':', line)[1].lstrip()
				organization = re.split('\s{2,}', organization)
				# print(organization)
				orgTwo = organization[0]
				orgThree = organization[1]
				# print(orgTwo)
				# print(orgThree)

			elif line.find('Designation') >= 0:
				designation = re.split(':', line)[1].lstrip()
				designation = re.split('\s{2,}', designation)
				desigTwo = designation[0]
				desigThree = designation[1]
				# print(desigTwo)
				# print(desigThree)

			elif line.find('Name') >= 0:
				name = re.split(':', line)[1].lstrip()
				name = re.split('\s{2,}', name)
				nameTwo = name[0]
				nameThree = name[1]
				# print(nameThree)
				# print(nameTwo)

		except:
			pass

	if line.find('Employment History') >= 0:
		job = lines[lineNumber + 2 : lineNumber + 6]
		desigOne = ''.join(job)
		# print(job)
	
	lineNumber += 1

# print(lines	)
orgOne = ""
infoOne = nameOne +',' + emailOne + ',' + mobOne + ',' + desigOne + ',' + orgOne
infoTwo = nameTwo + ',' + emailTwo + ',' + mobTwo + ',' + desigTwo + ',' + orgTwo
infoThree = nameThree + ',' + emailThree + ',' + mobThree + ',' + desigThree + ',' + orgThree


print(infoOne)
print(infoTwo)
print(infoThree)

with open('test.csv','w') as f:
	f.write(infoOne+'\n')
	f.write(infoTwo + '\n')
	f.write(infoThree + '\n')
