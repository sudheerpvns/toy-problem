#@author Sudheer P.V.N.S

import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru= {}

    def put(self,key,value):
        pass

    def get(self, key):
        pass
    
    def get_cache(self):
        pass
if __name__ == "__main__":
    obj = LRUCache(5)

l = ['one','two','three','four','five']
for i in range(1,6):
    obj.put(i,l[i-1])
obj.get_cache()

if 'one' == obj.get(1):
    print("Test case 1 passed")
else:
    print("Fialed 1")
if -1 == obj.get(6):
    print("Test case 2 passed")
else:
    print("Fialed 2")
obj.put(6,'six')
obj.get_cache()
if obj.get(1) == -1:
    print("Test case 3 passed")
else:
    print("Fialed 3")
