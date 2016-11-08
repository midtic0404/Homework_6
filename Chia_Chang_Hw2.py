#!/usr/bin/env python3
import sys
import re
import heapq
from urllib.request import urlopen

def process():
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test") as log:
        error_dict = dict()
        wordsArray = [] #big list storing each line as list
        for line in log:
            words = line.decode('utf-8')
            words = words.replace("\n"," ")
            wordsList = words.split(" ") #a list as a line separate by " "
            wordsArray.append(wordsList) #adding small list to big list
            
            if wordsList[12] in error_dict:
                error_dict[wordsList[12]] += 1

            if not wordsList[12] in error_dict:
                error_dict[wordsList[12]] = 0
                error_dict[wordsList[12]] += 1
        print(len(error_dict)) #test to see how many keys in dict 
        
def main():
    process()


if __name__ == "__main__":
    main()
    exit(0)
