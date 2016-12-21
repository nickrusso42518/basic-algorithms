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
        time complexity: best Ω(n), average Θ(n^2), worst O(n^2)
        space complexity: constant (sort in place), no recursion
    '''
    @staticmethod
    def sinking_sort( array ):
        
        # Needed to initialize the first iteration
        swapped = True
        
        # If we are swapping values, that means we aren't done
        while swapped:
            
            # Swap has not yet occurred
            swapped = False
            eprint("not done swapping")
            
            # Start at the second place in the array
            for i in range ( 1, len(array) ):
                eprint ("for i=1 to {0} i: {1}".format (len(array)-1, i ))
                
                # Test if the previous element is greater than the current
                if( array[i-1] > array[i] ):
                    eprint ("previous {0} > current {1}; swap".format(array[i-1], array[i]))
                    
                    # It was; swap the entries to sink big numbers
                    array[i], array[i-1] = array[i-1], array[i]
                    eprint("after swap: {0}".format( array ) )
                    
                    # Record that a swap occured to indicate that
                    #  we are not done. Note that this sort requires
                    #  an iteration to ensure the list is sorted; this
                    #  is guaranteed to be true when swapped is false.
                    swapped = True
        
        # Return the newly-sorted array       
        return array
    
    '''
    This algorithm sorts "array" by bubbling small numbers to the left (top)
    by swapping adjacent elements. The logic is identical to sinking_sort()
    but works by moving smaller elements to the left (reverse logic).
    Characteristics:
        time complexity: best Ω(n), average Θ(n^2), worst O(n^2)
        space complexity: constant (sort in place), no recursion
    '''   
    @staticmethod
    def bubble_sort( array ):
        
        # Needed to initialize the first iteration
        swapped = True
        
        # If we are swapping values, that means we aren't done
        while swapped:
            
            # Swap has not yet occurred
            swapped = False
            eprint("not done swapping")
            
            # Start at the first place in the array and go to the penultimate place
            for i in range ( len(array) - 1 ):
                eprint ("for i=0 to {0} i: {1}".format (len(array)-2, i ))
                
                # Test if the next field is less than the current
                if( array[i+1] < array[i] ):
                    eprint ("next {0} < current {1}; swap".format(array[i+1], array[i]))
                    
                    # It was; swap the entries to bubble up small numbers
                    array[i], array[i+1] = array[i+1], array[i]
                    eprint("after swap: {0}".format( array ) )
                    
                    # Record that a swap occured to indicate that
                    #  we are not done. Note that this sort requires
                    #  an iteration to ensure the list is sorted; this
                    #  is guaranteed to be true when swapped is false.
                    swapped = True

        # Return the newly-sorted array
        return array
    
    '''
    This algorithm sorts "array" by finding the lowest value in the array
    and swapping it with the first index of the "unsorted list". This
    unsorted list starts at the left and slowly shrinks as minimum
    elements are selected and swapped to the front. The sorted list grows
    from left to right commensurate with the shrinking of the unsorted list.
    Characteristics:
        time complexity: best Ω(n^2), average Θ(n^2), worst O(n^2)
        space complexity: constant (sort in place), no recursion
    '''
    @staticmethod
    def selection_sort( array ):
        
        # We can stop short since we are searching for the minimum
        #  each time. By the time we hit the n-1 element, the
        #  array is already sorted.
        for i in range( len(array) - 1 ):
            
            # Define the index which identifies the current
            #  minimum number. Assume it starts at i.
            imin = i
            eprint("for i=0 to {0}: i={1} imin={2}".format(len(array), i, imin )) 
            
            # Check everything after i for smaller values
            for j in range (i+1, len(array)):
                eprint("for j={0} to {1}: j={2} imin={3}".format(i+1, len(array), j, imin )) 
                
                # If we find an index representing a smaller
                #  element, store the new minimum value
                if ( array[j] < array[imin] ):
                    imin = j
                    eprint("imin=j={0}".format(j))
                    
            # At this point, imin is the minimum unsorted value
            #  Swap the value at index i and imin
            if( imin != i):
                array[i], array[imin] = array[imin], array[i]
                eprint("select {0} and swap with {1}".format(array[imin], array[i]))
                eprint("after swap: {0}".format( array ) )
        
        # Return the newly-sorted array 
        return array
    
    '''
    This algorithm sorts "array" by iterating through the array and
    inserting each element where it should go. When an element is inserted
    in front of several elements, the inner loop shifts values to the right.
    Characteristics:
        time complexity: best Ω(n), average Θ(n^2), worst O(n^2)
        space complexity: constant (sort in place), no recursion
    '''    
    @staticmethod
    def insertion_sort( array ):

        # Begin iterating through the array
        for i in range(len(array)):
            eprint("for i=0 to {0}: i={1}".format( len(array), i)) 
            
            # Set a marker equal to the current iterator
            j = i
            
            # The marker counts backwards from i to 0. If the
            #  previous value is greater than the current value,
            #  the elements are out of place. Iteratively swap
            # the values
            while( j > 0 and array[j-1] > array[j]):
                eprint("insert {0} by swapping with {1}. j={2}".format( array[j], array[j-1], j) )
                array[j-1], array[j] = array[j], array[j-1]
                eprint("after swap: {0}".format( array ) )
                j -= 1
        
        # Return the newly-sorted array 
        return array
    
    '''
    This algorithm sorts "array" by recursively halving the array. Each
    half is split down to a single element (which is sorted by definition).
    The individual sorted lists are merged back as the recursion stack
    unwinds which create longer sorted lists. This algorithm is guaranteed
    to be fast but does not sort in-place, which requires more memory.
    Characteristics:
        time complexity: best Ω(nlogn), average Θ(nlogn), worst O(nlogn)
        space complexity: linear (copy subarrays), log(n) recursion stack
    '''    
    @staticmethod
    def merge_sort( array ):
        an = len( array )

        if( an < 2 ):
            eprint( "base case: {0} < 2".format(an))
            return

        # Populate left array from 0 to the midpoint (not inclusive)
        #  In odd-length arrays, left will always be smaller
        left = [array[i] for i in range(0,int(an/2))]
        eprint ("left", left)
        
        # Populate right array from the midpoint (inclusive) to the end
        right = [array[i] for i in range(int(an/2),an)]
        eprint ("right", right)

        # sanity check, lenl + lenr == lena
        if( len(left) + len(right) != len(array) ):
            raise ValueError("sanity failure: {0} + {1} != {2}".format( 
            len(left), len(right), len(array)))

        # Sort the left and right sides independently
        #  The left sub array will be completely sorted before
        #  the right sub array even begins to be split.
        eprint ("Recursive left to merge_sort({0})".format(left))
        Sort.merge_sort(left)
        
        eprint ("Recursive right to merge_sort({0})".format(right))
        Sort.merge_sort(right)
        
        # Merge the two halves back into the higher-level array
        #  Method returns null; merges arrays in-place into "array"
        Sort._merge(array, left, right)

        # Return the newly-sorted array 
        return array
    
    """
    This method merges left and right sub arrays into the main
    array. Iteration begins at the beginning and compares the lowest
    values of left vs right, then adds the lowest into the main
    array. This process is impossible to perform without auxiliary
    arrays, which is why merge sort requires more memory than others.
    """    
    @staticmethod
    def _merge(array, left, right):
        eprint("_merge_fast begin: {0} and {1}".format( left, right ))
        
        # Initiate three iterators for each array
        ai, li, ri = 0, 0, 0
        
        # Store left and right array lengths
        ln = len(left)
        rn = len(right)
        
        # While there are still comparisons to be made
        while ( li < ln and ri < rn ):
        
            eprint("Testing {0} < {1}".format(left[li], right[ri]))
            if(left[li] < right[ri]):
                eprint(" true; choose {0}".format(left[li]))
                array[ai] = left[li]
                li += 1
            else:
                eprint(" false; choose {0}".format(right[ri]))
                array[ai] = right[ri]
                ri += 1
            ai += 1
        while (li < ln):
            eprint("add remaining left value: {0}".format(left[li]))
            array[ai] = left[li]
            li += 1
            ai += 1
        while (ri < rn):
            eprint("add remaining right value: {0}".format(right[ri]))
            array[ai] = right[ri]
            ri += 1
            ai += 1
            
        eprint("_merge_fast complete: {0}".format(array))
    
    """
    This technique selects the last element in the array as a "pivot"
    value, then determines which elements are less than or greater than
    the pivot value. These sublights are recursively sorted in similar
    fashion (select a pivot, partition the sublist, etc). The base case
    occurs when the list has only one element, which means that start
    index is greater or equal to the end index.
    Characteristics:
        time complexity: best Ω(nlogn), average Θ(nlogn), worst O(n^2)
        space complexity: constant (sort in place), log(n) recursion stack
    """    
    @staticmethod
    def quick_sort( array, start=0, end=-1 ):
        
        # Used to initialize "end" only once
        if (end == -1 ):
            end = len(array)-1
        
        # If start comes before end, we aren't done    
        if( start < end ):
            part = Sort._partition( array, start, end )
            eprint ("Recursive left with indices {0},{1}".format(start,part-1))
            Sort.quick_sort( array, start, part - 1 )
            eprint ("Recursive right with indices {0},{1}".format(part+1,end))
            Sort.quick_sort( array, part + 1, end )
        
        # Return the newly-sorted array     
        return array
    
    """
    This method takes the original array, along with start/end indices for
    framing purposes, then partitions that subarray. The process of partitioning
    first includes selecting a pivot (the last value is chosen). Then, each
    element in the array is tested against the pivot and moved to the left if
    it is less or equal to the pivot. This is done by swapping small values with
    the value at the partition index, which starts at the beginning of the subarray.
    Last, the pivot is swapped to the partition index; this has the nice side effect
    of being the final location of the pivot value.
    """        
    @staticmethod
    def _partition( array, start, end ):
        # First, choose the pivot (last value)
        
        eprint( "_partition {0} s={1} e={2}".format(array[start:end+1], start, end))
        
        # Initialize the pivot value and partition index
        pivot = array[end]
        part = start
        
        # Iterate over elements in the subarray
        for i in range(start, end):
            eprint("testing if {0} left of {1}".format(array[i], pivot))
            
            # Test for values that belong to the left of the pivot
            if( array[i] <= pivot ):
                
                # Swap the elements at the partition index with the current iterator
                eprint( " true, swap {0} and {1}".format(array[i], array[part]))
                array[i], array[part] = array[part], array[i]
                
                # Swap happened, so move the partition index to the right
                #  to set up for the next swap operation
                part += 1
                eprint( " after swap: {0}, part={1}".format(array,part))
        
        # The value at the current iterator is known to be greater than the pivot,
        #  so perform this final swap. This places the pivot in its final location.
        eprint ("final partition step; swap {0} and {1}".format(array[end], array[part]))  
        array[end], array[part] = array[part], array[end]
        eprint( "after swap: {0}, part={1}".format(array,part))
        
        # Return the partition index. quick_sort() needs this for recursive calls
        return part
    
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
            raise ValueError ("Sanity failure: array was None")
            
        eprint("** starting {0} **".format(self.work_method.__name__))
        eprint("initial array: {0}".format(array))  
          
        result = self.work_method( array )
        
        eprint("sorted array: {0}".format(result)) 
        eprint("** ending {0} **".format(self.work_method.__name__))
        return result
