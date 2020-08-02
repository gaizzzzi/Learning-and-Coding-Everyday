class dbLinkedlist:
    def __init__(self, val, _prev = None, _next = None):
        self.val = val
        self.prev = _prev
        self.next = _next
        
class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur_page = dbLinkedlist(homepage)

    def visit(self, url: str) -> None:
        if not self.cur_page.next or self.cur_page.next.val != url:
            self.cur_page.next = dbLinkedlist(url, self.cur_page)
        self.cur_page = self.cur_page.next

    def back(self, steps: int) -> str:
        step = 0
        while self.cur_page.prev and step < steps:
            self.cur_page = self.cur_page.prev
            step += 1
        return self.cur_page.val

    def forward(self, steps: int) -> str:
        step = 0
        while self.cur_page.next and step < steps:
            self.cur_page = self.cur_page.next
            step += 1
        return self.cur_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

class BrowserHistory:
    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.cur_page = 0
        self.pages_len = 1
    def visit(self, url: str) -> None:
        if self.cur_page == len(self.pages) - 1:
            self.pages.append(url)
            self.pages_len += 1
        elif self.pages[self.cur_page + 1] != url:
            self.pages[self.cur_page + 1] = url
            self.pages_len = self.cur_page + 2
        self.cur_page += 1

    def back(self, steps: int) -> str:
        step = 0
        while self.cur_page > 0 and step < steps:
            self.cur_page -= 1
            step += 1
        return self.pages[self.cur_page]

    def forward(self, steps: int) -> str:
        step = 0
        while self.cur_page < self.pages_len - 1 and step < steps:
            self.cur_page += 1
            step += 1
        return self.pages[self.cur_page]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

class BrowserHistory:
    def __init__(self, homepage: str):
        self.backpages = [homepage]
        self.forwardpages = []
        
    def visit(self, url: str) -> None:
        if self.forwardpages and self.forwardpages[-1] == url:
            self.forwardpages.pop()
        else:
            self.forwardpages = []
        
        self.backpages.append(url)
            
    def back(self, steps: int) -> str:
        step = 0
        while len(self.backpages) > 1 and step < steps:
            self.forwardpages.append(self.backpages.pop())
            step += 1
        return self.backpages[-1]

    def forward(self, steps: int) -> str:
        step = 0
        while self.forwardpages and step < steps:
            self.backpages.append(self.forwardpages.pop())
            step += 1
        return self.backpages[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)