#!/usr/bin/python

'''
File: Search.py
Author: Nicholas Russo
Description: This class extends Worker by adding a target value
used for searching. It defines several static methods which can
be passed to the constructor for execution during a test series.
'''

from Worker import Worker

class Search(Worker):
   
    '''
    Walk the array from front to back to find a specific target.
    This algorithm is guaranteed to work regardless of the current
    state of the array.
    '''
    @staticmethod
    def linear_search( array, target ):
        
        # Iterate over the list front to back
        for i in range(len(array)):
            
            # If we find the element, return the array index
            if( array[i] == target ):
                return i
        
        # Element not found, return -1
        return -1
    
    '''
    Recursively divide the array into halves to quickly find the
    target value. This algorithm ONLY works on sorted arrays.
    The input must be sorted from smallest to largest or else
    the algorithm will not return the correct value. This method
    does not test for sorted-ness as this defeats the purpose of
    having an efficient search algorithm in the first place.
    '''
    @staticmethod    
    def binary_search( array, target, left=0, right=-1 ):
        
        # Need to initialize the right boundary, but only once
        #  Would have been cool to use "right=len(array)-1 in the method line
        #  but this technique is not supported
        if( right == -1 ):
            right = len(array) - 1
        
        # Compute the middle index by finding the midpoint between
        #  left and right limits, and removing any floating point   
        middle = int((left+right)/2)
        
        # The element was not found; prevent infinite recursio
        if( left > right ):
            return -1
            
        # If array[middle] is less than the target, go right
        elif( array[middle] < target ):
            return Search.binary_search( array, target, middle + 1, right)
            
        # If array[middle] is greater than the target, go left
        elif( array[middle] > target ):
            return Search.binary_search( array, target, left, middle - 1)
            
        # We must have found the proper value
        else:
            return middle 
    
    '''
    Constructor is a pass-through for Worker with the exception of
    adding a target. This "target" is the value that the search
    algorithm is trying to find within the arrays found inside
    the input file defined inside "path".
    '''
    def __init__(self, path, work_method, target, ifile_type = Worker.LINEAR ):
        Worker.__init__(self, path, work_method, ifile_type)
        self.target = target

    '''
    Prepend the target value and invoke the parent method.
    '''        
    def __str__(self):
        string = "Target value: {0}\n".format(self.target)
        return string + super().__str__()


    '''
    Test the array for nonexistence. If it is valid, run the
    selected work method to find the target value
    '''
    def _run_test(self, array):
        if ( array == None ):
            return -1
        return self.work_method( array, self.target )
        