'''
Created on Oct 21, 2014

@author: computer
'''

import glob
import fileinput
import nltk   
from urllib.request import urlopen
from sys import argv

def createOutPutFiles():
    files = glob.glob("./training/*.html")
    print(files)
    for file in files:
        print(file)
        txt = open(file)
        s= remove_tags(txt.read())
        t = open("./trainingOut/" + file.replace("./training", ""), "w+")
        print(s)
        t.write(s)

def remove_tags(input_text):
    # convert in_text to a mutable object (e.g. list)
    s_list = list(input_text)
    i,j = 0,0
    while i < len(s_list):
        # iterate until a left-angle bracket is found
        if s_list[i] == '<':
            while s_list[i] != '>':
                # pop everything from the the left-angle bracket until the right-angle bracket
                s_list.pop(i)
            # pops the right-angle bracket, too
            s_list.pop(i)
        else:
            i=i+1
    # convert the list back into text
    join_char=''
    return join_char.join(s_list)
 
#Now just pass an HTML formatted text through this function .It remove the tags and return the string
if __name__ == '__main__':
#     createOutPutFiles()
    print("HI")

