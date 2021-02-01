class LRU_Cache(object):

    def __init__(self, capacity):
        self.data = {}
        self.order = {}
        self.capacity = capacity

        self.highest_order = 0
        self.lowest_order = 1

        self.filled = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.  
        dat = self.data.get(key, None)
        
        if dat:
            self.highest_order += 1
            if self.order.get(self.data[key]['order'], None):
                del self.order[self.data[key]['order']]

                # increase the lowest order until it is present in the order dict
                while self.lowest_order not in self.order and self.order:
                    self.lowest_order += 1

                if not self.order:
                    self.lowest_order = self.highest_order

            self.order [self.highest_order] = key
            self.data[key]['order'] = self.highest_order
            return dat ['data']
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        dat = self.data.get(key, None)
        if not dat and self.filled < self.capacity:
            self.highest_order += 1
            self.data[key] = {'data': value, 'order': self.highest_order}
            self.order [self.highest_order] = key

            self.filled += 1
            
        
        elif not dat and self.capacity == self.filled:
            if self.capacity <= 0:
                return

            lowest_key = self.order [self.lowest_order]
            del self.order[self.lowest_order]
            # increase the lowest order until it is present in the order dict
            del self.data[lowest_key]
            while self.lowest_order not in self.order and self.order:
                self.lowest_order += 1

            if not self.order:
                self.lowest_order = self.highest_order

            self.data[key] = {'data': value, 'order': self.highest_order}
            self.order [self.highest_order] = key
            self.highest_order += 1 


def test():
    # Test Case 1
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    # returns 1
    print ("Pass" if (1 == our_cache.get(1)) else "Fail")

    # returns 2 
    print ("Pass" if (2 == our_cache.get(2)) else "Fail")

    # returns -1 because 9 is not present in the cache 
    print ("Pass" if (-1 == our_cache.get(9)) else "Fail")
    
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
 
    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print ("Pass" if (-1 == our_cache.get(3)) else "Fail")      
    
    # Test case 2
    our_cache = LRU_Cache(1)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    
    # returns -1
    print ("Pass" if (-1 == our_cache.get(1)) else "Fail")

    # returns -1 
    print ("Pass" if (-1 == our_cache.get(2)) else "Fail")

    # returns -1 because 9 is not present in the cache 
    print ("Pass" if (-1 == our_cache.get(9)) else "Fail")

    # returns 4
    print ("Pass" if (4 == our_cache.get(4)) else "Fail")
    
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
 
    # returns 6
    print ("Pass" if (6 == our_cache.get(6)) else "Fail") 

    # Test case 3
    our_cache = LRU_Cache(0)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    
    # returns -1
    print ("Pass" if (-1 == our_cache.get(1)) else "Fail")

    # returns -1 
    print ("Pass" if (-1 == our_cache.get(2)) else "Fail")

    # returns -1 because 9 is not present in the cache 
    print ("Pass" if (-1 == our_cache.get(9)) else "Fail")

    # returns 4
    print ("Pass" if (-1 == our_cache.get(4)) else "Fail")
    
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
 
    # returns 6
    print ("Pass" if (-1 == our_cache.get(6)) else "Fail")  
test()