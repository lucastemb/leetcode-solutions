class MyCircularQueue:

    def __init__(self, k: int):
        self.s=[-1]*k
        self.items_in=0
        self.top=0
        self.back=0
        self.insert = 0

        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.s[self.items_in] = value
        self.items_in+=1
        return True 

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        for i in range(len(self.s)-1):
            self.s[i] = self.s[i+1]
        self.items_in-=1
        return True
        

    def Front(self) -> int:
        return self.s[0]
        

    def Rear(self) -> int:
        return self.s[self.items_in-1]
        

    def isEmpty(self) -> bool:
        if self.items_in == 0: 
            return True
        return False
        

    def isFull(self) -> bool:
        if self.items_in == len(self.s):
            return True
        return False
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()