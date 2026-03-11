class Node:
    def __init__(self, site: str):
        self.data = site
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.tab = Node(homepage)
        self.current = self.tab
        self.last = self.tab
        

    def visit(self, url: str) -> None:
        self.current.next = None
        self.last = self.current
        self.last.next = Node(url)
        self.last.next.prev = self.last
        self.last= self.last.next
        self.current = self.last
        
        

    def back(self, steps: int) -> str:
        while(self.current.prev and steps>0):
            self.current = self.current.prev
            steps-=1
        return self.current.data
        

    def forward(self, steps: int) -> str:
        while(self.current.next and steps>0):
            self.current = self.current.next
            steps-=1
        return self.current.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)