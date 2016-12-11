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

class Worker:
    
    MICRO = 1000000
    MILLI = 1000
    LINEAR = 1
    GRAPH_MATRIX = 2
    
    '''
    
    '''
    def __init__(self, path, work_method, ifile_type):
         
        # Assign variables as inputs are valid
        if( ifile_type == Worker.LINEAR ):
            parse_path = self._parse_linear
        elif( ifile_type == Worker.GRAPH_MATRIX ):
            parse_path = self._parse_graph_matrix
            
        self.work_list = parse_path( path )
        self.set_work_method( work_method )
        self.clear_all_history()
        
    '''
    
    '''  
    def clear_time_history(self):
        self.suite_start_time = 0
        self.suite_end_time = 0
        self.test_start_times = list()
        self.test_end_times = list()
        
    def clear_all_history(self):
        self.test_count = 0
        self.pass_count = 0
        self.clear_time_history()
        self.result_list = list()
        
    def set_work_method(self, work_method):
        self.work_method = work_method
        
    '''
    
    '''  
    def get_result_list(self):    
        return self.result_list
        
    '''
    Test # time: 
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
    
    '''        
    def get_suite_elapsed_time(self):
        return self.suite_end_time - self.suite_start_time
        
    '''
    
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
        
    def get_test_count(self):
        return self.test_count
        
    def get_pass_count(self):
        return self.pass_count
        
    def get_fail_count(self):
        return self.test_count - self.pass_count
        
    '''
    
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
    
    '''
    def _run_test(self, array):
        pass
        
    def _parse_linear(self, path):
        with open( path ) as handle:
            line = "start"
            
            work_list = list()
            while line is not "":
                line = handle.readline().strip()
                if line is not "":
                    work_list.append( [int(s) for s in line.split()] )       
        
        return work_list
        
    def _parse_graph_matrix(self, path):
        # TODO
        raise NotImplementedError()
        
        
    