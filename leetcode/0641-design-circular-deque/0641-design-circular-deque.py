class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
class MyCircularDeque:

    def __init__(self, k: int):
        # self.header = None
        self.front = None
        self.last = None
        self.size = 0   
        self.mx =k    
        

    def insertFront(self, value: int) -> bool:
        temp = Node(value)
        if(not self.isFull()):
            temp.next = self.front
            if(self.front):
                self.front.prev = temp
            self.front = temp
            if(not self.last):
                self.last = self.front
            self.size+=1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        temp = Node(value)
        if(not self.isFull()):
            if(self.last):
                self.last.next = temp
                temp.prev = self.last
                self.last = self.last.next
            else:
                self.last = temp
                self.front = self.last
            self.size+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if(not self.isEmpty()):
            self.front = self.front.next
            if self.front:
                self.front.prev = None
            if(self.size == 1):
                self.last = None
            self.size-=1
            return True
        return False

    def deleteLast(self) -> bool:
        if(not self.isEmpty()):
            self.last = self.last.prev
            if self.last:
                self.last.next = None
            if(self.size == 1):
                self.front = None
            self.size -=1
            return True
        return False

        

    def getFront(self) -> int:
        if(self.size>0):
            return self.front.val
        return -1
        

    def getRear(self) -> int:
        if(not self.isEmpty()):
            return self.last.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
 
    def isFull(self) -> bool:
        return self.size == self.mx
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()