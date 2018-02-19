#!/usr/bin/python
# -*- coding: utf-8 -*-
import openpyxl
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
wb = openpyxl.load_workbook('./Corpus/36.xlsx')
ws = wb.active
text_column = ws['AB']
rows = len(text_column)

with open('./Results/nltk_sa.txt','a+') as f:
	for row in range(rows):
		text = text_column[row].value
		f.write('\n'+text.encode('utf-8')+'\n')
		sentiment = sia.polarity_scores(text)
		for k in sentiment:
			line = '{0}: {1} '.format(k, sentiment[k])
			f.write(line)
	f.close()
