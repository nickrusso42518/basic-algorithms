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
    
    # Define the sort algorithms to test
    sort_alg_list = [
        Sort.quick_sort,
        Sort.merge_sort,
        Sort.selection_sort,
        Sort.insertion_sort,
        Sort.sinking_sort,
        Sort.bubble_sort,
        ]
    
    # Iterate over all algorithms specified above    
    for sort_alg in sort_alg_list:
        
        # Create a new instance of a sort object with the input file
        #  and the specific sorting algorithm
        sort = Sort(argv[1], sort_alg)
        
        # Run all tests
        sort.run_suite()
        
        # Print the output
        print(sort)
        print()

# Executation starts here
main( sys.argv )