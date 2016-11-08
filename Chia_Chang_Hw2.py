#!/usr/bin/env python3
import sys
import re
from urllib.request import urlopen

def process():
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test") as log:
        test = set()
        for line in log:
            words = line.decode('utf-8').split(" ")
            test.add(words[7])

        print(test)
        
def main():
    process()


if __name__ == "__main__":
    main()
    exit(0)
