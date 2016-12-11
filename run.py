#!/usr/bin/python

'''
File: run.py
Author: Nicholas Russo
Description: This file is used for testing and comparison of
different search, sort, and other algorithms defined within
this project.
'''

import os
import sys
from Search import Search
from Sort import Sort

def main( argv ):
    
    # Test for 2 CLI arguments (script name and input file)
    # Test for existence of the input file
    if( len( argv ) != 2 or not os.path.isfile( argv[1] ) ):
        raise ValueError( "Invalid arguments: length or input file" )
    
    
    search = Search(argv[1],Search.linear_search,4)
    search.run_suite()
    print(search)
    
    sort = Sort(argv[1],Sort.sinking_sort)
    sort.run_suite()
    print(sort)
    
    sort = Sort(argv[1],Sort.bubble_sort)
    sort.run_suite()
    print(sort)


# Executation starts here
main( sys.argv )