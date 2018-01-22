import PyPDF2 
import textract
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords\

nltk.download()

filename = sys.argv[1]


pdfFileObj = open(filename, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

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

#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

else:
   text = textract.process(filename, method='tesseract', language='eng')

# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.



#The word_tokenize() function will break our text phrases into #individual words

tokens = word_tokenize(text)

#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';',':','[',']',',']

#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords

stop_words = stopwords.words('english')

#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.

keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]


newfile = open("output.txt", "w")
newfile.write(str(keywords))
newfile.close()
