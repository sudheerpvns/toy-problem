#@author Sudheer P.V.N.S

import collections

class LRUCache:
    def __init__(self, capacity, delta=None):
        self.capacity = capacity
        self.delta = delta
        self.dict = {}
        self.list= []

