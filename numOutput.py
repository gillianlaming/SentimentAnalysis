#calculated the percentate correct of our sentiment analysis
import re
import sys
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

 sc = SparkContext()
 A = sc.textFile(sys.argv[1])
 B = A.map(lambda line: line[1])
 print(B.count())
 C = B.map(lambda line: (line.split("\t")[0], line.split("\t")[1]))
 D = C.filter(lambda line: line[0]==line[1])
 val = float(D.count())/B.count()
 print(val)

