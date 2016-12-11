#!/usr/bin/python

'''
File: Sort.py
Author: Nicholas Russo
Description: 
'''

from Worker import Worker

class Sort(Worker):
    
    @staticmethod
    def sinking_sort( array ):
        # Sink big numbers to the right (bottom)
        sarray = list(array)
        swapped = True
        
        while swapped:
            swapped = False
            for i in range ( 1, len(sarray) ):
                if( sarray[i-1] > sarray[i] ):
                    sarray[i], sarray[i-1] = sarray[i-1], sarray[i]
                    swapped = True
                
        return sarray
        
    @staticmethod
    def bubble_sort( array ):
        # Bubble small numbers to the left (top)
        sarray = list(array)
        swapped = True
        
        while swapped:
            swapped = False
            for i in range ( len(sarray) - 1 ):
                if( sarray[i+1] < sarray[i] ):
                    sarray[i], sarray[i+1] = sarray[i+1], sarray[i]
                    swapped = True

        return sarray
    
    @staticmethod
    def selection_sort( array ):
        return -1
        
    @staticmethod
    def insertion_sort( array ):
        return -1
        
    @staticmethod
    def merge_sort( array ):
        return -1
        
    @staticmethod
    def quick_sort( array ):
        return -1
    
    '''
    
    '''
    def __init__(self, work_list, work_method):
        Worker.__init__(self, work_list)
        self.work_method = work_method

    '''
    Test # time: 
    '''        
    def __str__(self):
        string = "Algorithm: {0}\n".format(self.work_method.__name__)
        return string + super().__str__()


    '''
    
    '''
    def _run_test(self, array):
        if ( array == None ):
            return -1
        return self.work_method( array )
        

        
    