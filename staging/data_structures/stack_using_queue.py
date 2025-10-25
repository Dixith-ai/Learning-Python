from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if self.empty():
            return None
        return self.queue.popleft()
    
    def top(self):
        if self.empty():
            return None
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

class StackUsingTwoQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def push(self, x):
        self.queue1.append(x)
    
    def pop(self):
        if self.empty():
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result
    
    def top(self):
        if self.empty():
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        result = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result
    
    def empty(self):
        return len(self.queue1) == 0
    
    def size(self):
        return len(self.queue1)

class StackUsingQueueOptimized:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        size = len(self.queue)
        self.queue.append(x)
        
        for _ in range(size):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if self.empty():
            return None
        return self.queue.popleft()
    
    def top(self):
        if self.empty():
            return None
        return self.queue[0]
    
    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

stack1 = StackUsingQueue()
stack2 = StackUsingTwoQueues()
stack3 = StackUsingQueueOptimized()

elements = [1, 2, 3, 4, 5]

print("Stack using single queue:")
for elem in elements:
    stack1.push(elem)
    print(f"Pushed {elem}, top: {stack1.top()}")

while not stack1.empty():
    print(f"Popped: {stack1.pop()}")

print("\nStack using two queues:")
for elem in elements:
    stack2.push(elem)
    print(f"Pushed {elem}, top: {stack2.top()}")

while not stack2.empty():
    print(f"Popped: {stack2.pop()}")

print("\nStack using optimized queue:")
for elem in elements:
    stack3.push(elem)
    print(f"Pushed {elem}, top: {stack3.top()}")

while not stack3.empty():
    print(f"Popped: {stack3.pop()}")
