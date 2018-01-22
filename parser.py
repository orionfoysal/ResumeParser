import PyPDF2
import sys
#write a for-loop to open many files -- leave a comment if you'd #like to learn how

filename = sys.argv[1]
print(filename)

#filename = 'Shariful IslamFoysalProfile.pdf' 

#open allows you to read the file

pdfFileObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all #the pages

num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.

if text != "":
   text = text


# file = open("output.txt", "w")
# file.write(text)
# file.close()

#text = "Orionfoysal@gmail.com +440123456789 8801912293318 pilabsbd@gmail.com"

import re

email = ""
email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print("Email ")
print(email[0])


mobile = ""
mobile = re.findall(r'(?:\+?88)?[0]\d{10}',text)
#handling the cases when mobile number is not given
#mobile = re.findall(r'(?:\+?44)?[07]\d{9,13}', text)
print("Mobile : ")
print(mobile)
