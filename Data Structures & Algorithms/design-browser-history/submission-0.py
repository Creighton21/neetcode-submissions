class ListNode:
    def __init__(self, url = '', next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_location = ListNode(homepage, None, None)
        self.backwards_steps = 0
        self.forwards_steps = 0

    def visit(self, url: str) -> None:
        new_node = ListNode(url, None, self.current_location) # Create new ode
        self.current_location.next = new_node # Clears forward, new url is forward history
        self.current_location = new_node # Move my current location
        self.forwards_steps = 0 # Cannot go forward
        self.backwards_steps = self.backwards_steps + 1 # can go 1 more step back
        

    def back(self, steps: int) -> str:
        steps_to_go_back = steps if self.backwards_steps >= steps else self.backwards_steps

        current = self.current_location
        steps_moved = 0
        while steps_moved != steps_to_go_back:
            current = current.prev
            steps_moved += 1

        self.backwards_steps = self.backwards_steps - steps_moved
        self.forwards_steps = self.forwards_steps + steps_moved
        self.current_location = current

        return self.current_location.url

    def forward(self, steps: int) -> str:
        steps_to_go_forward = steps if self.forwards_steps >= steps else self.forwards_steps

        current = self.current_location
        steps_moved = 0
        while steps_moved != steps_to_go_forward:
            current = current.next
            steps_moved += 1

        self.backwards_steps = self.backwards_steps + steps_moved
        self.forwards_steps = self.forwards_steps - steps_moved
        self.current_location = current

        return self.current_location.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)