#!/usr/bin/python

'''
File: run.py
Author: Nicholas Russo
Description: 
'''

import os
import sys
from Search import Search
from random import randint

def main( argv ):
    
    # Test for 2 CLI arguments (script name and input file)
    # Test for existence of the input file
    if( len( argv ) != 2 or not os.path.isfile( argv[1] ) ):
        raise ValueError( "Invalid arguments: length or input file" )
    
    
    search = Search(argv[1],Search.binary_search,4)
    search.run_suite()
    print(search)

    '''
    for t in range(40):
        string = ""
        for i in range(20):
            string += str(randint(-20,20)) + " "
        print (string)
    '''

# Executation starts here
main( sys.argv )