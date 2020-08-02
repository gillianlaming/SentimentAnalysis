#this file stems the pos/neg word list
import re
import sys
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def getValue(str1):
	if(str1 != u'\xef'):
		str2 = str1.strip()
		stemmer = PorterStemmer()
		return stemmer.stem(str2)
	else:
		return "" 
		
	
sc=SparkContext()
A = sc.textFile(sys.argv[1])
C = A.flatMap(lambda line: line.splitlines())
D = C.map(lambda line: getValue(line))
E = D.map(lambda line: line.strip())
E.saveAsTextFile(sys.argv[2])

