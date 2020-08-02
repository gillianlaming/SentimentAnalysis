#Max M, Justin S, Gillian L

import re
import sys
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def removeWord(str1):
	negation_words = ["not", "no", "nor", "neither", "none", "wasn't", "wouldn't", "couldn't", "never", "nobody"]
        newstr=""
	#source: nltk.org
	stemmer = PorterStemmer()
        para=str1.split(" ")
        f=open("english.stop","r")
        contents=f.readlines()
        for word in para:
                for check in contents:
                        if check.strip()== word:
				if (word not in negation_words):
					word=""
                       # print("word is " + word + " check is " + check)
		if word!="":
			newstr = newstr + " "+ stemmer.stem(word)
        f.close()
        return newstr



if __name__ == "__main__":
	if len(sys.argv)<3:
		print ("usage: pyspark fileIn fileOut")
		exit(-1)

	sc = SparkContext()
	A = sc.wholeTextFiles(sys.argv[1])
	B= A.filter(lambda line: len(line[1].split(" "))>=50)
	C = B.map(lambda line: (line[0].encode("ascii","ignore"), re.sub("\W", " ", line[1])))
	D=C.map(lambda line: (line[0].split("/")[6], line[0].split("/")[5], line[1].encode("ascii","ignore")))
	E=D.map(lambda line: line[0].split(" ")[0][2] + "\t" + line[1] + "\t" + removeWord(str(line[2].lower())) )
	E.saveAsTextFile(sys.argv[2])
	sc.stop()
	quit()

