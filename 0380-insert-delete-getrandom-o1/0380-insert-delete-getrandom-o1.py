class RandomizedSet:

    def __init__(self):
        self.nums=set()
        self.vals=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.nums.add(val)
            self.vals.append(val)
            return True
        else: 
            return False
        

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False
        else: 
            self.nums.discard(val)
            self.vals.remove(val)
            return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()