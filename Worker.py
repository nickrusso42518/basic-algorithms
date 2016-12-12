#!/usr/bin/python

'''
File: Worker.py
Author: Nicholas Russo
Description: This base class is meant to be ABSTRACT and should
not be instantiated directly. It provides a method for parsing
input files and maintaining a list of jobs (each job could be 
a list, a matrix, or anything else which represents input data).
The class maintains several timers and pass/fail statistics which
help for comparing algorithmic performance.
'''

import time
import sys

DEBUG_TOGGLE = True

class Worker:
    
    MICRO = 1000000
    MILLI = 1000
    LINEAR = 1
    GRAPH_MATRIX = 2
    
    @staticmethod
    def eprint( *args, **kwargs):
        if DEBUG_TOGGLE:
            print( *args, file=sys.stderr, **kwargs )
    
    '''
    Base constructor which initializes relevant variables. The
    ifile_type is relevant as it determines how to parse the file.
    Some algorithms work on linear (1d) arrays while others require
    matrix (2d) arrays or even linked data structures. The work_method
    is the actual algorithm that gets run during each iteration or
    a test suite. This can be a search, sort, etc. The history data
    is statistics on passes, fails, elapsed times, etc.
    '''
    def __init__(self, path, work_method, ifile_type):
         
        # Assign variables as inputs are valid
        if( ifile_type == Worker.LINEAR ):
            parse_path = self._parse_linear
        elif( ifile_type == Worker.GRAPH_MATRIX ):
            parse_path = self._parse_graph_matrix
            
        self.work_list = parse_path( path )
        self.set_work_method( work_method )
        
        # Quick way to initialize variables
        self.clear_all_history()
        
    '''
    Resets all times to zero. The per-test time lists are
    reinstantiated which effectively erases them. This method does not
    change the work method, ifile_type, or test statistics.
    '''  
    def clear_time_history(self):
        self.suite_start_time = 0
        self.suite_end_time = 0
        self.test_start_times = list()
        self.test_end_times = list()
    
    '''
    Clear the time history plus the results. This method does not
    change the work method or ifile_type.
    '''     
    def clear_all_history(self):
        self.test_count = 0
        self.pass_count = 0
        self.clear_time_history()
        self.result_list = list()
    
    '''
    This method is used for updating the work_method (algorithm)
    without having to reinstantiate the Worker object. This might
    be useful for capturing aggregate statistics for all tests.
    '''
    def set_work_method(self, work_method):
        self.work_method = work_method
        
    '''
    If only the results are required, use this method. "results"
    this context refers to whatever was returned by the work_method.
    For example, a search algorithm would return an index of the element
    if found, while a sort would return the array of sorted elements.
    '''  
    def get_result_list(self):    
        return self.result_list
        
    '''
    Return a string this object in the following format:
    Algorithm: (work_method name)
    Test R: P in T us (C = test run number, P = passes, T = elapsed time in us)
    Total of P/C tests passed in T us (C = total test cases, P = passes, T = elapsed time in us)
    '''        
    def __str__(self):
        string = "Algorithm: {0}\n".format(self.work_method.__name__)
        count = 1
        times = self.get_test_elapsed_times()
        for i in range( len( times ) ):
            passed = self.result_list[i] != -1
            string += "Test {0}: {1} in {2} us\n".format(count, passed, times[i] * Worker.MICRO)
            count += 1
            if passed:
                self.pass_count += 1
        
        suite_time = self.get_suite_elapsed_time() * Worker.MICRO
        string += "Total of {0}/{1} tests passed in {2} us".format( self.pass_count, self.test_count, suite_time )
        return string

    '''
    Returns the elapsed time that the entire suite required to run.
    '''        
    def get_suite_elapsed_time(self):
        return self.suite_end_time - self.suite_start_time
        
    '''
    Return a list of all elapsed times per test. The list returned has the same length
    as the start/end time lists; it represents the difference of the two.
    '''        
    def get_test_elapsed_times(self):
        # Assert lengths are the same
        test_elapsed_times = list()
        for t in range( len( self.test_start_times ) ):
            
            # Assert 't' is an integer
            if( not isinstance( t, int ) ):
                raise ValueError( "t is not an int: {0}".format ( type(t) ) )
            
            test_elapsed_times.append( self.test_end_times[t] - self.test_start_times[t] )
    
        return test_elapsed_times
    
    '''
    Returns the total number of tests run.
    '''    
    def get_test_count(self):
        return self.test_count
        
    '''
    Returns the total number of tests passed.
    '''        
    def get_pass_count(self):
        return self.pass_count
        
    '''
    Returns the total number of tests failed.
    '''
    def get_fail_count(self):
        return self.test_count - self.pass_count
        
    '''
    Runs the entire test suite. Each test contained within the work_list
    is executed with its results stored in a list. This method is also
    the timer for both test suite and individual test run times.
    '''
    def run_suite(self):
        self.test_count = 0
        self.suite_start_time = time.time()
        for array in self.work_list:
            self.test_start_times.append( time.time() )
            self.result_list.append( self._run_test( array ) )
            self.test_end_times.append( time.time() )
            self.test_count += 1
        self.suite_end_time = time.time()
        
    '''
    Private method which is not implemented deliberately, rather than
    introduce abstract methods/classes. The method should run an
    individual test based on whatever input is required.
    '''
    def _run_test(self, input):
        raise NotImplementedError("child class should override this")

    '''
    Reads lines from a file and breaks individual elements apart
    into arrays for every row. The input should be values separated
    by single spaces, such as "1 5 7 0 -5 567".
    '''        
    def _parse_linear(self, path):
        with open( path ) as handle:
            line = "start"
            
            work_list = list()
            while line is not "":
                line = handle.readline().strip()
                if line is not "":
                    work_list.append( [int(s) for s in line.split()] )       
        
        return work_list
    
    '''
    Reads lines from a file and breaks individual elements apart
    into matrixes for every chunk of input. Matrices are separated
    by the sentinel "ZZZ" in the input files.
    '''    
    def _parse_graph_matrix(self, path):
        # TODO
        raise NotImplementedError()
 