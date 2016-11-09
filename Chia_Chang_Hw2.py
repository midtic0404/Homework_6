#!/usr/bin/env python3
import sys
import re
import heapq
from urllib.request import urlopen


def ReturnNum(a):
    return a[1]



def process():
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.full") as log:
        error_dict = dict()
        wordsArray = [] #big list storing each line as list
        for line in log:
            words = line.decode('utf-8')
            parts = words.partition('client')
            checkparts = parts[2] #string to be check
        
           # pat = re.compile('/[\w+/.-]+')#test from that site
            match = re.search('/[a-zA-Z][\w+/._~-]+',parts[2])
            if match:
                errorpath = match.group()
                
                if errorpath not in error_dict:
                    error_dict[errorpath] = 1
                else:
                    error_dict[errorpath] += 1
            
        error_list = list(error_dict.items())
        sort_list = sorted(error_list, key=ReturnNum)
        sort_list.reverse()
        
        print("*** Top 25 page errors ***")
        for i in range(25):
            print("Count: ", sort_list[i][1], "  ", "Page:  ", sort_list[i][0])

        
def main():
    process()


if __name__ == "__main__":
    main()
    exit(0)
