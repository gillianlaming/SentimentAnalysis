import re
import sys
import json
import gzip
from pyspark import SparkContext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def removeWord(str1):
    newstr=""
	#source: nltk.org
	stemmer = PorterStemmer()
    para=str1.split(" ")
    f=open("english.stop","r")
    contents=f.readlines()
    for word in para:
        for check in contents:
            if check.strip()==word:
                ##stuff goes here
                word=""
                # print("word is " + word + " check is " + check)
    if word!="":
        newstr = newstr + " "+ stemmer.stem(word)
    return newstr




if __name__ == "__main__":
    if len(sys.argv)<3:
        print ("usage: pyspark fileIn fileOut")
        exit(-1)




    sc = SparkContext()
        # A = sc.wholeTextFiles(sys.argv[1])
        # B= A.filter(lambda line: len(line[1].split(" "))>=50)
        # C = B.map(lambda line: (line[0].encode("ascii","ignore"), re.sub("\W", " ", line[1])))
        # D=C.map(lambda line: (line[0].split("/")[6], line[0].split("/")[5], line[1].encode("ascii","ignore")))
        # E=D.map(lambda line: line[0].split(" ")[0][2] + "\t" + line[1] + "\t" + removeWord(str(line[2].lower())) )
        # E.saveAsTextFile(sys.argv[2])



    A = sc.textFile(sys.argv[1])
    B = A.map(lambda line: line.split('\t')) 
    C = B.map(lambda line: (line[0].encode("ascii","ignore"), line[1].encode("ascii","ignore")))
    D = C.filter(lambda line: len(line[1].split(" "))>=50)
    E = D.map(lambda line: (line[0], re.sub("\W", " ", line[1].lower())))
    F=D.map(lambda line: line[0] + "\t" + removeWord(str(line[1])))




    # C = B.filter(lambda line: len(line[1].split(" "))>= 50)
    # C.take(5)
    # D = C.map(lambda line: line)

#D = C.map(lambda line: (line.split('\t')[1], line.split('\t')[2]))
    #D = C.map(lambda line: (line[0], getValue(str(line[1]))))
    F.saveAsTextFile(sys.argv[2])
    sc.stop()
    quit()

