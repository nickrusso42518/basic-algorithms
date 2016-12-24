#!/usr/bin/python


class Node:
    def __init__(self, d, n = None):
        self.data = d
        self.next = n
      
    # property decorators  
    def get_data(self):
        return self.data
        
    def set_data(self, d):
        self.data = d
        
    def get_next(self):
        return self.next
        
    def set_next(self, n):
        self.next = n
        
class LinkedList:
    def __init__(self, *datalist):
        
        # Sanity check; stop processing on empty input
        if( datalist == None or len(datalist) == 0 ):
            self.head = None
            self.tail = None
            self.size = 0
            return
        
        # Create the first Node and assign the head pointer to it
        self.head = Node(datalist[0])
        self.tail = self.head
        self.size = 1
        
        # Start iterating at the head
        cur = self.head
        for i in range(len(datalist)-1):
            
            # Create a new node and add it to the list
            new_node = Node(datalist[i+1])
            cur.set_next( new_node )
            
            # Advance the pointer
            cur = cur.get_next()
            
            # Keep updating the tail (not the head) and the size
            self.tail = cur
            self.size += 1
            
    def clone(self):
        cur = self.get_head()
        datalist = list()
        while cur:
            datalist.append( cur.get_data() )
            cur = cur.get_next()
            
        return LinkedList(datalist)
            
    def __str__(self):
        cur = self.get_head()
        result = ""
        while cur:
            result += str( cur.get_data() ) + " "
            cur = cur.get_next()
            
        result += "(h={0} t={1} n={2})".format(self.head.get_data(), self.tail.get_data(), self.size)
        return result
        
    def __len__(self):
        return self.size
        
    def __add__(self, other):
        # Append other to the end of self
        if( other == None ):
            return None
        
        other_head = other.get_head()
        self._sanity_check_node( other_head )
        self.get_tail().set_next( other_head )
        
        cur = other_head
        while cur:
            self._set_tail( cur )
            self.size += 1
            cur = cur.get_next()
        
        return self
        
    def _sanity_check_node(self, n):
        if n == None:
            raise TypeError( "node was none" )
        
        if not isinstance(n, Node):
            raise TypeError( "n is wrong type: {0}".format(type(n)))
            
        nnext = n.get_next()
        if nnext != None and not isinstance(nnext, Node):
            raise TypeError( "n.get_next() is wrong type: {0}".format(type(nnext)))
        
    def get_head(self):
        return self.head
        
    def _set_head(self, n):
        self._sanity_check_node( n )
        self.head = n
        
    def get_tail(self):
        return self.tail
        
    def _set_tail(self, n):
        self._sanity_check_node( n )
        self.tail = n
        
    def append(self, n):
        self._sanity_check_node( n )
        self.get_tail().set_next( n )
        self._set_tail( n )
        self.size += 1
        return self.size
        
    def prepend(self, n):
        self._sanity_check_node( n )
        n.set_next( self.get_head() )
        self._set_head( n )
        self.size += 1
        return self.size
        
    def insert(self, n, i):
        
        self._sanity_check_node( n )
        
        if( i < 0 ):
            return self.prepend( n )
        elif( i >= self.size ):
            return self.append( n )
        
        # Move cur to the previous node right before the
        #  insertion point
        cur = self.get_head()
        j = 0
        while j < i:
            j += 1
            cur = cur.get_next()
        
        n.set_next( cur.get_next() )
        cur.set_next( n )
            
        self.size += 1
        return self.size
        
    def remove(self, d):
        cur = self.get_head()
        
        while cur and cur.get_next():
            if ( cur.get_next().get_data() == d ):
                cur.set_next( cur.get_next().get_next() )
                self.size -= 1
                return self.size
                
            cur = cur.get_next()
            
        return -1
        
    def find_data(self, d):
        
        cur = self.get_head()
        i = 0
        while cur:
            if ( cur.get_data() == d ):
                return i
            else:
                i += 1
            cur = cur.get_next()
        return -1
        
    def make_list(self):
        result = list()
        cur = self.get_head()
        while cur:
            result.append( cur.get_data() )
            cur = cur.get_next()
            
        return result
        
    def make_tuple(self):
        return tuple( self.make_list() )
        
    def make_set(self):
        return set( self.make_list() )
            

def main():
    ll = LinkedList(1,4,2,6,5)
    ll1 = LinkedList()
    print(ll)

    ll.append(Node(9))
    print(ll)
    
    ll.prepend(Node(-55))
    print(ll)
    
    print( ll.find_data(2) )
    print( ll.find_data(88) )
    
    ll.insert(Node(3),3)
    ll.insert(Node(3),3)
    ll.insert(Node(3),3)
    print (ll)
    
    ll.insert(Node(70),70)
    print (ll)
    
    ll.insert(Node(8),-9)
    print (ll)
    
    print (ll.make_list())
    print (ll.make_tuple())
    print (ll.make_set())
    
    print( ll.remove(3) )
    print (ll)
    print( ll.remove(3) )
    print (ll)
    print( ll.remove(3) )
    print (ll)
    print( ll.remove(3) )
    print (ll)
    
    ll2 = LinkedList(41,42,43)
    ll3 = ll + ll2
    print (ll3)
    print (id(ll),id(ll2),id(ll3))
    
    ll4 = ll1.clone()
    #print (ll1, ll4)
    #print( id(ll1), id(ll4))
    
main()