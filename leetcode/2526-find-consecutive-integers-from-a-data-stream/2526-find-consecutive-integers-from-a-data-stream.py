from collections import deque 
class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.q.append(num)
        if num != self.value:
            self.count +=1
        while(len(self.q) > self.k):
            n = self.q.popleft()
            if(n!=self.value):
                self.count-=1
            
        if(len(self.q) >= self.k and self.count == 0 ):
            return True
        return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)