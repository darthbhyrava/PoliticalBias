import os
import sys

text=[]
sent=[]

with open('../Results/26.xml', 'r') as txt:
	for line in txt:
		if '<sentence id' in line:
			sent.append(line.strip())
	txt.close()

with open('../Results/26.xml', 'r') as txt:
	for line in txt:
		if '<text>' in line:
			line = (line.replace('</text>', '').replace('<text>','')).strip()
			text.append(line)
	txt.close()

