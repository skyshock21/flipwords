#!/usr/bin/env python
#
# flipwords.py
# A script to read in a text file, reverse all the words,
# and output the reversed words

import sys,argparse

# Function Defs
def flipwords():
    wordlist = args.file.read().split(' ') #read in file as list
    newList=[]                             #initialize empty placeholder list
    for i in wordlist:                     #iterate over list flipping element order
        newList.append(i[::-1])
    print(' '.join(newList))               #output joined new list elements as string

# CLI arguments & arg parser
ex = '''example:
python flipwords.py file.txt'''
parser = argparse.ArgumentParser(prog='flipwords',
                                description='Flips words in a text file backwards.',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
parser.add_argument('file', type=argparse.FileType('r'))
parser.set_defaults(func=flipwords)
args = parser.parse_args()

def main():
    args.func()

if __name__ == "__main__":
    sys.exit( main() )
