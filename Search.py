#!/usr/bin/python

'''
File: Search.py
Author: Nicholas Russo
Description: 
'''

from Worker import Worker

class Search(Worker):
    
    @staticmethod
    def linear_search( array, target ):
        # Iterate over the list front to back
        for i in range(len(array)):
            
            # If we find the element, return the array index
            if( array[i] == target ):
                return i
        
        # Element not found, return -1
        return -1
    
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
    
    '''
    def __init__(self, work_list, work_method, target):
        Worker.__init__(self, work_list)
        self.work_method = work_method
        self.target = target

    '''
    Test # time: 
    '''        
    def __str__(self):
        string = "Algorithm: {0}\n".format(self.work_method.__name__)
        string += "Target value: {0}\n".format(self.target)
        return string + super().__str__()


    '''
    
    '''
    def _run_test(self, array):
        return self.work_method( array, self.target )
        

        
    