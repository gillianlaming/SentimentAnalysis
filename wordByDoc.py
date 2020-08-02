#Max M, Justin S, Gillian L
#based off of slides and reference material
#calculates word frequency by homework
import re
import sys
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def tokenize(s):
	return re.split("\\W+", s.lower())

if __name__ == "__main__":
    if len(sys.argv)<3:
        print ("usage: pyspark fileIn fileOut")
        exit(-1)
    sc = SparkContext()
    Z = sc.wholeTextFiles(sys.argv[1])
    A = Z.map(lambda line : line[1])
    B = A.flatMap(lambda line: line.splitlines())
    C = B.map(lambda value: (str(value.split('\t')[0]), tokenize(str(value.split('\t')[2]))))
    print(C.take(1))
    term_frequency = C.flatMapValues(lambda x:x).countByValue()
    f= open("pleasehalp.txt", "w+")
    for val in term_frequency.items(): 
	f.write(str(val[0][0])+ " " + str(val[0][1]) + "\t" + str(val[1]) + "\n")
    f.close()
	
    sc.stop()
    quit()

