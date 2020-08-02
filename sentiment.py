import re
import sys
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def getValue(str1):
	 score = 0
	 total = 0
	 flag = 1
	 negation_words = ["not", "no", "nor", "neither", "none", "wasn't", "wouldn't", "couldn't", "never", "nobody"]
	 posWords=open("pos-words.txt","r")
	 negWords=open("neg-words.txt","r")
	 stemmer = PorterStemmer()
	 para=str1.split(" ")
	 contents = posWords.readlines()
	 posStem = [""]
	 
	 for word in contents:
		 posStem.append(stemmer.stem(word.strip()))
	
         contents2 = negWords.readlines()
	 negStem = [""]
	 for word in contents2:
		 negStem.append(stemmer.stem(word.strip()))
	 posWords.close()
	 negWords.close()
	 prevWordNeg = 0
	 for word in para:
		 total += 1
		 if (word in posStem):
			 if prevWordNeg: 
				 score -=1
			 else: 
				 score +=1 
		 elif (word in negStem):
			 if prevWordNeg: 
				 score +=1
			 else: 
				 score -=1 
			
		 if(word in negation_words): 
			 prevWordNeg = 1
		 else:
			 prevWordNeg=0
		 
         
	 average = float(score)/total
	 if(average<=0.08): 
		 return "negative"
	 elif(average<=0.12):
		 return "neutral"
	 else: 
		 return "positive"
	 
if __name__ == "__main__":
	if len(sys.argv)<3:
		print ("usage: pyspark fileIn fileOut")
		exit(-1)

	sc = SparkContext()
	A = sc.textFile(sys.argv[1])
	B = A.flatMap(lambda line: line.split('\n'))
	C = B.map(lambda line: (line.split('\t')[1], line.split('\t')[2]))
	D = C.map(lambda line: (line[0], getValue(str(line[1]))))
	D.saveAsTextFile(sys.argv[2])
	sc.stop()
	quit()

