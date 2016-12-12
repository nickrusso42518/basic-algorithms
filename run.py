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
    
    sort_alg_list = [
        Sort.selection_sort,
        Sort.insertion_sort,
        Sort.sinking_sort,
        Sort.bubble_sort
        ]
        
    for sort_alg in sort_alg_list:
        sort = Sort(argv[1], sort_alg)
        sort.run_suite()
        print(sort)
        print()


# Executation starts here
main( sys.argv )