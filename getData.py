#this file 
import re
import sys
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

sc = SparkContext()
A=sc.textFile(sys.argv[1])
count = A.count()
B=A.filter(lambda line: line[2])
print(B.take(1))
print(count/B.count())


