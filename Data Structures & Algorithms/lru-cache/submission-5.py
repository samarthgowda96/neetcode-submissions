from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()
        

    def get(self, key: int) -> int:
        
        if key in self.d:
            self.d.move_to_end(key)

            return self.d[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
        else:
            if len(self.d) == self.capacity:
                self.d.popitem(last=False)
        self.d[key]=value
        
