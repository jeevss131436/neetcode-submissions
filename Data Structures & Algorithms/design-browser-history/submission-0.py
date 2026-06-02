class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.prev = self.curr
        self.curr.next = new_node
        new_node.next = None
        self.curr = new_node
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev is None:
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val
         

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next is None:
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)