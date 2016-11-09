#!/usr/bin/env python3
import sys
import re
import heapq
from urllib.request import urlopen

def process():
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.full") as log:
        error_dict = dict()
        wordsArray = [] #big list storing each line as list
        for line in log:
            words = line.decode('utf-8')
            parts = words.partition('client')
            checkparts = parts[2] #string to be check
        
           # pat = re.compile('/[\w+/.-]+')#test from that site
            match = re.search('/[\w+/._~-]+',parts[2])
            if match:
                errorpath = match.group()
                
                if errorpath not in error_dict:
                    error_dict[errorpath] = 1
                else:
                    error_dict[errorpath] += 1
            

        if "/var/www/html/_c21_" in error_dict:
            print("Yes" , error_dict["/var/www/html/_c21_"])
        else:
            print("no")

        
def main():
    process()


if __name__ == "__main__":
    main()
    exit(0)
