"""
This program takes a url as parameter
Arg:
    A web link
Result:
    print out the top 25 errors from the error log

"""


#!/usr/bin/env python3
import sys
import re
import heapq
from urllib.request import urlopen


def ReturnNum(a):
    """
    For use in sorting the list
    """
    return a[1]


def help():
    """
    Prompt to user to enter a url for parameter
    """
    print("Please enter the url as parameter")



def process(url):
    """
    Process that take a url link with error logs and print out
    the top 25 errors from the log

    Arg:
        a url link
    Result:
        print out the top 25 errors
    """
    with urlopen(url) as log:
        error_dict = dict()
        wordsArray = [] #big list storing each line as list
        for line in log:
            words = line.decode('utf-8')
            parts = words.partition('client')
            checkparts = parts[2] #string to be check
        
           
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

        
def main(url):
    """
    Main to run the process
    """
    process(url)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        help()
    else:
        main(sys.argv[1])
        exit(0)
