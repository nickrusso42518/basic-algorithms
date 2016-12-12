#!/usr/bin/python

'''
File: Sort.py
Author: Nicholas Russo
Description: This class extends Worker. It defines several static methods 
which can be passed to the constructor for execution during a test series.
'''

from Worker import Worker
eprint = Worker.eprint

class Sort(Worker):
    
    '''
    This algorithm sorts "array" by sinking big numbers to the right (bottom)
    by swapping adjacent elements. Each iteration guarantees that the largest
    number is moved as far right as possible. Other numbers will be swapped
    along the way too.
    '''
    @staticmethod
    def sinking_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        eprint("** starting sinking_sort **")
        
        # Needed to initialize the first iteration
        swapped = True
        
        # If we are swapping values, that means we aren't done
        while swapped:
            
            # Swap has not yet occurred
            swapped = False
            eprint("not done swapping")
            
            # Start at the second place in the array
            for i in range ( 1, len(sarray) ):
                eprint ("for i=1 to {0} inc: {1}".format (len(sarray)-1, i ))
                
                # Test if the previous element is greater than the current
                if( sarray[i-1] > sarray[i] ):
                    eprint ("previous {0} > current {1}; swap".format(sarray[i-1], sarray[i]))
                    
                    # It was; swap the entries to sink big numbers
                    sarray[i], sarray[i-1] = sarray[i-1], sarray[i]
                    
                    # Record that a swap occured to indicate that
                    #  we are not done. Note that this sort requires
                    #  an iteration to ensure the list is sorted; this
                    #  is guaranteed to be true when swapped is false.
                    swapped = True
        
        # Return the newly-sorted array  
        eprint("** ending sinking_sort **")      
        return sarray
    
    '''
    This algorithm sorts "array" by bubbling small numbers to the left (top)
    by swapping adjacent elements. The logic is identical to sinking_sort()
    but works by moving smaller elements to the left (reverse logic).
    '''   
    @staticmethod
    def bubble_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        eprint("** starting bubble_sort **")  
        
        # Needed to initialize the first iteration
        swapped = True
        
        # If we are swapping values, that means we aren't done
        while swapped:
            
            # Swap has not yet occurred
            swapped = False
            eprint("not done swapping")
            
            # Start at the first place in the array and go to the penultimate place
            for i in range ( len(sarray) - 1 ):
                eprint ("for i=0 to {0} inc: {1}".format (len(sarray)-2, i ))
                
                # Test if the next field is less than the current
                if( sarray[i+1] < sarray[i] ):
                    eprint ("next {0} < current {1}; swap".format(sarray[i+1], sarray[i]))
                    
                    # It was; swap the entries to bubble up small numbers
                    sarray[i], sarray[i+1] = sarray[i+1], sarray[i]
                    
                    # Record that a swap occured to indicate that
                    #  we are not done. Note that this sort requires
                    #  an iteration to ensure the list is sorted; this
                    #  is guaranteed to be true when swapped is false.
                    swapped = True

        # Return the newly-sorted array
        eprint("** ending bubble_sort **")  
        return sarray
    
    @staticmethod
    def selection_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        
        # We can stop short since we are searching for the minimum
        #  each time. By the time we hit the n-1 element, the
        #  array is already sorted
        for i in range( len(sarray) - 2 ):
            
            # Define the index which identifies the current
            #  minimum number. Assume it starts at i.
            imin = i
            
            # Check everything after i for smaller values
            for j in range (i+1, len(sarray)):
                
                # If we find an index representing a smaller
                #  element, store the new minimum value
                if ( sarray[j] < sarray[imin] ):
                    imin = j
                    
            # At this point, imin is the minimum unsorted value
            #  Swap the value at index i and imin
            if( imin != i):
                sarray[i], sarray[imin] = sarray[imin], sarray[i]
        
        return sarray
        
    @staticmethod
    def insertion_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        
        # Begin iterating through the array
        for i in range(len(sarray)):
            
            # Set a marker equal to the current iterator
            j = i
            
            # The marker counts backwards from i to 0. If the
            #  previous value is greater than the current value,
            #  the elements are out of place. Iteratively swap
            # the values
            while( j > 0 and sarray[j-1] > sarray[j]):
                sarray[j-1], sarray[j] = sarray[j], sarray[j-1]
                j -= 1
        
        return sarray
        
    @staticmethod
    def merge_sort( array ):
        return -1
        
    @staticmethod
    def quick_sort( array ):
        return -1
    
    '''
    Constructor is a pass-through for Worker. No additional
    information is added within the Sort class at this time.
    '''
    def __init__(self, path, work_method, ifile_type=Worker.LINEAR):
        Worker.__init__(self, path, work_method, ifile_type)

    '''
    Test the array for nonexistence. If it is valid, run the
    selected work method to sort the specific array.
    ''' 
    def _run_test(self, array):
        if ( array == None ):
            return -1
        return self.work_method( array )
