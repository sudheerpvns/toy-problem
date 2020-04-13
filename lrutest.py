from lrucache import *
class testLRU:
    def test(self,obj):
        l = ['one','two','three','four','five']
        for i in range(1,6):
            obj.put(i,l[i-1])
        assert -1 == obj.get(1), "Failed 1st case"
        assert -1 == obj.get(6),"Failed 2nd Test case"
        obj.put(6,'six')
        assert obj.get(2) == -1, "Failed 3rd Test Case"
        k = [obj.cache[i] for i in obj.cache]
        print(k)
        assert k == ['four','five','six'], 'Failed LRU'
        print("ALL TESTS PASSED")
if __name__ == "__main__":
     obj = LRUCache(3)
     p = testLRU()
     p.test(obj)
