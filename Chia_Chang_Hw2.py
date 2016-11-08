#!/usr/bin/env python3
import sys
import re
from urllib.request import urlopen

def process():
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test") as log:
        for line in log:
            words = line.decode('utf-8').split()
            print(words)


def main():
    process()


if __name__ == "__main__":
    main()
    exit(0)
