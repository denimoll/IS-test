#Убираем строки, содержащие заглавие страниц: Chapter и Appendix
"""
find = "Chapter"
ENC = "utf-8"
for x in range (1, 8):
	x=7
	inputFile = str(x) + ".txt"
	outputFile = str(x) + "q.txt"
	print("hello" + str(x))
	with open(inputFile, encoding=ENC) as input, open(outputFile, "w", encoding=ENC) as output:
		for line in input:
			if find.lower() not in line.lower():
				output.write(line)
"""

import random
from googletrans import Translator
translator = Translator()

numberOfChapter = random.randint(1,7)
Chapter = {1:"Threats, Attacks, and Vulnerabilities",2:"Technologies and Tools",3:"Architecture and Design",4:"Identity and Access Management",5:"Risk Management",6:"Cryptography and PKI",7:"Practice Test"}

fileQ = open(str(numberOfChapter)+"q.txt")
fileA = open(str(numberOfChapter)+"a.txt")
textQ = fileQ.read()
textA = fileA.read()
numberOfQ = 6666

while (textQ.find(str(numberOfQ)+". ") == -1):
	numberOfQ = random.randint(1,200)
print("Chapter: " + str(Chapter.get(numberOfChapter)) + ".\n\nQuestion:")
if (textQ.find(str(numberOfQ+1)+". ") != -1):
	Question = textQ[textQ.find(str(numberOfQ)+ ". "):textQ.find(str(numberOfQ+1)+ ". ")]
	Answer = textA[textA.find(str(numberOfQ)+ ". "):textA.find(str(numberOfQ+1)+ ". ")]
else:
        Question = textQ[textQ.find(str(numberOfQ)+ ". "):len(textQ)]
        Answer = textA[textA.find(str(numberOfQ)+ ". "):len(textA)]
print(Question)

enText = "Chapter: " + str(Chapter.get(numberOfChapter)) + ".\n\nQuestion:\n" + str(Question)
ruText = translator.translate(enText, dest='ru')
print(ruText.text)

print("\nAnswer:")
print(Answer)

enText = "\nAnswer:\n" + str(Answer) + "\n"
ruText = translator.translate(enText, dest='ru')
print(ruText.text)
