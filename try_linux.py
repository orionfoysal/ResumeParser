import math
import re
import sys
import pdftotext

filename = sys.argv[1]
#Load the PDF
with open(filename, "rb") as f:
	pdf = pdftotext.PDF(f)

# Iterate over all the pages
doc = ""
for page in pdf:
	doc += page

print(doc)

lines = doc.split('\n')

lineNumber = 0

nameOne = lines[2].lstrip()
# print(nameOne)

reference = math.nan 

for line in lines:
	if lineNumber < 10:
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
				mobile = re.split(': | \s{2,}', line)
				mobTwo = mobile[2]
				mobThree = mobile[3]
				# print(mobTwo)
				# print(mobThree)

			elif line.find('EMail') >= 0:
				email = re.split(': | \s{2,}', line)
				emailTwo = email[2]
				emailThree = email[3]
				# print(emailTwo)
				# print(emailThree)
			
			elif line.find('Organization') >= 0:
				organization = re.split(': | \s{2,}', line)
				# print(organization)
				orgTwo = organization[2]
				orgThree = organization[3]
				# print(orgTwo)
				# print(orgThree)

			elif line.find('Designation') >= 0:
				designation = re.split(': | \s{2,}', line)
				desigTwo = designation[2]
				desigThree = designation[3]
				# print(desigTwo)
				# print(desigThree)

			elif line.find('Name') >= 0:
				name = re.split(':|\s{2,}', line)
				nameTwo = name[2].lstrip()
				nameThree = name[3].lstrip()
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
