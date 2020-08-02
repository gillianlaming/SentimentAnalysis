import re
import sys
from pyspark import SparkContext

sc = SparkContext()
A  = sc.wholeTextFiles(sys.argv[1])
B = A.map(lambda line: line[1])
M = B.flatMap(lambda line: line.splitlines())
counter = M.count()
C = M.map(lambda line: str(line))
D = C.map(lambda line: line.split("u")[1])
E = D.map(lambda line: (line.split("\'")[1], line.split("\'")[3]))
F = E.filter(lambda line: line[0]==line[1])
count2= F.count()
G = F.map(lambda line: (line, float(count2)/counter))
G.saveAsTextFile(sys.argv[2])

