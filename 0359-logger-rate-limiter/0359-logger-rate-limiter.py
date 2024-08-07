class Logger:

    def __init__(self):
        self.words={}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.words: 
            self.words[message] = timestamp
            return True
        elif self.words[message] + 10 <= timestamp:
            self.words[message] = timestamp
            return True
        else: 
            return False
            
                

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)