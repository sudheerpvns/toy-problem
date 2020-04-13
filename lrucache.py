#@author Sudheer P.V.N.S


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru= {}

    def put(self,key,value):
        if(len(self.cache) >= self.capacity):
                old_key = min(self.lru.keys(), key= lambda k:self.lru[k])
                self.cache.pop(old_key)
                self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] =self.tm
        self.tm += 1 

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1
    
    def get_cache(self):
        for i in self.lru:
            print(i,self.cache[i])

if __name__ == "__main__":
    obj = LRUCache(3)

l = ['one','two','three','four','five']
for i in range(1,6):
    obj.put(i,l[i-1])
print("Current Cache:")
obj.get_cache()
print('#'*20)
if -1 == obj.get(1):
    print("Test case 1 passed")
else:
    print("Fialed 1")
if -1 == obj.get(6):
    print("Test case 2 passed")
else:
    print("Fialed 2")

obj.put(6,'six')
print("Current Cache:")
obj.get_cache()
print('#'*20)
if obj.get(2) == -1:
    print("Test case 3 passed")
else:
    print("Fialed 3")
k = [obj.cache[i] for i in obj.cache]
if k == ['four','five','six']:
    print('test case 4 passed')
else:
    print('Failed 4')
