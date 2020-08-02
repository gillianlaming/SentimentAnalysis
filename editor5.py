import re
import sys
from pyspark import SparkContext

def getVal(str1): 
  if str1=="5.0" or str1== "4.0":
  	return "positive"
  elif str1=="3.0": 
  	return "neutral"
  else: 
  	return "negative"


sc = SparkContext()
A  = sc.wholeTextFiles(sys.argv[1])
B = A.map(lambda line: line[1])
M = B.flatMap(lambda line: line.splitlines())
counter = M.count()
C = M.map(lambda line: str(line))
D = C.map(lambda line: line.split("u")[1])
E = D.map(lambda line: (line.split("\'")[1], line.split("\'")[3]))
F = E.map (lambda line: (getVal(str(line[0])), getVal(str(line[1]))))
G = F.filter(lambda line: line[0] == line[1])
count2= G.count()
G = F.map(lambda line: (line, float(count2)/counter))
G.saveAsTextFile(sys.argv[2])

