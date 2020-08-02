import re
import sys
from pyspark import SparkContext

def getValue(str1):
	 score = 0
	 total = 0
	 flag = 1
         posWords=open("pos-words.txt","r")
	 negWords=open("neg-words.txt","r")
	 stemmer = PorterStemmer()
         contents = posWords.readlines()
	 posStem = [""]
         for word in contents:
		 posStem.append(stemmer.stem(word.strip()))
	
         contents2 = negWords.readlines()
	 negStem = [""]
	 for word in contents2:
		 negStem.append(stemmer.stem(word.strip()))
         if (word in posStem):
		 return word
			 
	 else:
		 return ""
	 posWords.close()
	 negWords.close()
	 

		 
		
		
	 
if __name__ == "__main__":
	if len(sys.argv)<3:
		print ("usage: pyspark fileIn fileOut")
		exit(-1)
	sc = SparkContext()
	A = sc.textFile(sys.argv[1])
	B = A.flatMap(lambda line: line.split('\n'))
	C = B.map(lambda line: line.split('\t')[2])
	D = C.flatMap(lambda line: line.split())
        E = D.map(lambda word: (word, 1))
        F = E.reduceByKey(lambda v1,v2: v1+v2)
       
	G.saveAsTextFile(sys.argv[2])
	sc.stop()
	quit()

