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
    Characteristics:
        time complexity: best O(n^2), average O(n^2), worst O(n^2)
        space complexity: O(1)
    '''
    @staticmethod
    def sinking_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        eprint("** starting sinking_sort **")
        eprint("initial array: {0}".format(sarray))
        
        # Needed to initialize the first iteration
        swapped = True
        
        # If we are swapping values, that means we aren't done
        while swapped:
            
            # Swap has not yet occurred
            swapped = False
            eprint("not done swapping")
            
            # Start at the second place in the array
            for i in range ( 1, len(sarray) ):
                eprint ("for i=1 to {0} i: {1}".format (len(sarray)-1, i ))
                
                # Test if the previous element is greater than the current
                if( sarray[i-1] > sarray[i] ):
                    eprint ("previous {0} > current {1}; swap".format(sarray[i-1], sarray[i]))
                    
                    # It was; swap the entries to sink big numbers
                    sarray[i], sarray[i-1] = sarray[i-1], sarray[i]
                    eprint("after swap: {0}".format( sarray ) )
                    
                    # Record that a swap occured to indicate that
                    #  we are not done. Note that this sort requires
                    #  an iteration to ensure the list is sorted; this
                    #  is guaranteed to be true when swapped is false.
                    swapped = True
        
        # Return the newly-sorted array  
        eprint("sorted array: {0}".format(sarray)) 
        eprint("** ending sinking_sort **")      
        return sarray
    
    '''
    This algorithm sorts "array" by bubbling small numbers to the left (top)
    by swapping adjacent elements. The logic is identical to sinking_sort()
    but works by moving smaller elements to the left (reverse logic).
    Characteristics:
        time complexity: best O(n^2), average O(n^2), worst O(n^2)
        space complexity: O(1)
    '''   
    @staticmethod
    def bubble_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        eprint("** starting bubble_sort **")
        eprint("initial array: {0}".format(sarray))  
        
        # Needed to initialize the first iteration
        swapped = True
        
        # If we are swapping values, that means we aren't done
        while swapped:
            
            # Swap has not yet occurred
            swapped = False
            eprint("not done swapping")
            
            # Start at the first place in the array and go to the penultimate place
            for i in range ( len(sarray) - 1 ):
                eprint ("for i=0 to {0} i: {1}".format (len(sarray)-2, i ))
                
                # Test if the next field is less than the current
                if( sarray[i+1] < sarray[i] ):
                    eprint ("next {0} < current {1}; swap".format(sarray[i+1], sarray[i]))
                    
                    # It was; swap the entries to bubble up small numbers
                    sarray[i], sarray[i+1] = sarray[i+1], sarray[i]
                    eprint("after swap: {0}".format( sarray ) )
                    
                    # Record that a swap occured to indicate that
                    #  we are not done. Note that this sort requires
                    #  an iteration to ensure the list is sorted; this
                    #  is guaranteed to be true when swapped is false.
                    swapped = True

        # Return the newly-sorted array
        eprint("sorted array: {0}".format(sarray))  
        eprint("** ending bubble_sort **")  
        return sarray
    
    '''
    This algorithm sorts "array" by finding the lowest value in the array
    and swapping it with the first index of the "unsorted list". This
    unsorted list starts at the left and slowly shrinks as minimum
    elements are selected and swapped to the front. The sorted list grows
    from left to right commensurate with the shrinking of the unsorted list.
    Characteristics:
        time complexity: best O(n^2), average O(n^2), worst O(n^2)
        space complexity: O(1)
    '''
    @staticmethod
    def selection_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        eprint("** starting selection_sort **")
        eprint("initial array: {0}".format(sarray))  
        
        # We can stop short since we are searching for the minimum
        #  each time. By the time we hit the n-1 element, the
        #  array is already sorted.
        for i in range( len(sarray) - 1 ):
            
            # Define the index which identifies the current
            #  minimum number. Assume it starts at i.
            imin = i
            eprint("for i=0 to {0}: i={1} imin={2}".format(len(sarray), i, imin )) 
            
            # Check everything after i for smaller values
            for j in range (i+1, len(sarray)):
                eprint("for j={0} to {1}: j={2} imin={3}".format(i+1, len(sarray), j, imin )) 
                
                # If we find an index representing a smaller
                #  element, store the new minimum value
                if ( sarray[j] < sarray[imin] ):
                    imin = j
                    eprint("imin=j={0}".format(j))
                    
            # At this point, imin is the minimum unsorted value
            #  Swap the value at index i and imin
            if( imin != i):
                sarray[i], sarray[imin] = sarray[imin], sarray[i]
                eprint("select {0} and swap with {1}".format(sarray[imin], sarray[i]))
                eprint("after swap: {0}".format( sarray ) )
        
        eprint("sorted array: {0}".format(sarray)) 
        eprint("** ending selection_sort **") 
        return sarray
    
    '''
    This algorithm sorts "array" by iterating through the array and
    inserting each element where it should go. When an element is inserted
    in front of several elements, the inner loop shifts values to the right.
    '''    
    @staticmethod
    def insertion_sort( array ):
        
        # Copy the array into a new array so the original values dont change
        sarray = list(array)
        eprint("** starting insertion_sort **")
        eprint("initial array: {0}".format(sarray))  
        
        # Begin iterating through the array
        for i in range(len(sarray)):
            eprint("for i=0 to {0}: i={1}".format( len(sarray), i)) 
            
            # Set a marker equal to the current iterator
            j = i
            
            # The marker counts backwards from i to 0. If the
            #  previous value is greater than the current value,
            #  the elements are out of place. Iteratively swap
            # the values
            while( j > 0 and sarray[j-1] > sarray[j]):
                eprint("insert {0} by swapping with {1}. j={2}".format( sarray[j], sarray[j-1], j) )
                sarray[j-1], sarray[j] = sarray[j], sarray[j-1]
                eprint("after swap: {0}".format( sarray ) )
                j -= 1
        
        eprint("sorted array: {0}".format(sarray)) 
        eprint("** ending insertion_sort **") 
        return sarray
        
    @staticmethod
    def merge_sort( array ):
        # TODO
        raise NotImplementedError()
        
    @staticmethod
    def quick_sort( array ):
        # TODO
        raise NotImplementedError()
    
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
