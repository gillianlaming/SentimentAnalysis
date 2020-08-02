#this file counts the positive/negative reviews based on ground truth
import re
import sys
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
     
if __name__ == "__main__":
    if len(sys.argv)<3:
        print ("usage: pyspark fileIn fileOut")
        exit(-1)

    sc = SparkContext()
    A = sc.wholeTextFiles(sys.argv[1])
    M = A.map(lambda line: line[1])
    B = M.flatMap(lambda line: line.splitlines())
    C = B.map(lambda line: line.split('\t')[1])
    D = C.map(lambda line: (line,1))
    E = D.reduceByKey(lambda v1,v2: v1 + v2)
    E.saveAsTextFile(sys.argv[2])
    sc.stop()
    quit()

