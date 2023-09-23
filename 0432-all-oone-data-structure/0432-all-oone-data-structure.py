class AllOne:
    def __init__(self): #initialization function count
        self.counts={}
        self.lookup = collections.defaultdict(set)
        self.maxIndex=0
        self.minIndex=0

    def inc(self, key: str) -> None: #increment works O(1) time insertion and retrieval into a hashmap 
        if key not in self.counts: 
            self.counts[key]=1
            self.lookup[1].add(key)
            self.minIndex=1
            if self.maxIndex < 1:
                self.maxIndex=1
        else: 
            self.lookup[self.counts[key]].remove(key)
            if self.minIndex==self.counts[key] and len(self.lookup[self.counts[key]]) == 0:
                self.minIndex+=1
            self.counts[key]+=1
            self.lookup[self.counts[key]].add(key)
            if self.counts[key] > self.maxIndex:
                self.maxIndex=self.counts[key]

        

    def dec(self, key: str) -> None:
        self.lookup[self.counts[key]].remove(key)
        if self.minIndex == self.counts[key] and len(self.lookup[self.counts[key]]) == 0:
            self.minIndex-=1
        if self.counts[key] == self.maxIndex and len(self.lookup[self.counts[key]]) == 0:
            self.maxIndex-=1
        self.counts[key]-=1

        if self.counts[key] > 0: 
            self.lookup[self.counts[key]].add(key)
        else:
            del self.counts[key]

    def getMaxKey(self) -> str:
        if len(self.lookup[self.maxIndex]) > 0:
            return next(iter(self.lookup[self.maxIndex]))
        return ""
        

    def getMinKey(self) -> str:
        if len(self.lookup[self.minIndex]) > 0:
            return next(iter(self.lookup[self.minIndex]))
        if self.minIndex == 0 and len(self.counts) > 0: 
            while len(self.lookup[self.minIndex]) == 0:
                self.minIndex +=1
            return next(iter(self.lookup[self.minIndex]))
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()