from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
      
        self.capacity=capacity
        self.queue=deque()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usekey(key)
            return self.cache[key]
        else:
            return -1
        
    def usekey(self,key):
        self.queue.remove(key)
        self.queue.append(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key]=value
            self.usekey(key)
        else:
            
            
            if len(self.queue)>=self.capacity:
                eviction_key=self.queue.popleft()
                del self.cache[eviction_key]
            self.queue.append(key)
            self.cache[key]=value

        
