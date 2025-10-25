class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x):
        self.stack1.append(x)
    
    def dequeue(self):
        if self.empty():
            return None
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
    
    def front(self):
        if self.empty():
            return None
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]
    
    def empty(self):
        return not self.stack1 and not self.stack2
    
    def size(self):
        return len(self.stack1) + len(self.stack2)

class QueueUsingStackOptimized:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    
    def enqueue(self, x):
        self.input_stack.append(x)
    
    def dequeue(self):
        if self.empty():
            return None
        
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        return self.output_stack.pop()
    
    def front(self):
        if self.empty():
            return None
        
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        
        return self.output_stack[-1]
    
    def empty(self):
        return not self.input_stack and not self.output_stack
    
    def size(self):
        return len(self.input_stack) + len(self.output_stack)

class QueueUsingSingleStack:
    def __init__(self):
        self.stack = []
    
    def enqueue(self, x):
        self.stack.append(x)
    
    def dequeue(self):
        if self.empty():
            return None
        
        if len(self.stack) == 1:
            return self.stack.pop()
        
        item = self.stack.pop()
        result = self.dequeue()
        self.stack.append(item)
        return result
    
    def front(self):
        if self.empty():
            return None
        
        if len(self.stack) == 1:
            return self.stack[-1]
        
        item = self.stack.pop()
        result = self.front()
        self.stack.append(item)
        return result
    
    def empty(self):
        return not self.stack
    
    def size(self):
        return len(self.stack)

queue1 = QueueUsingStack()
queue2 = QueueUsingStackOptimized()
queue3 = QueueUsingSingleStack()

elements = [1, 2, 3, 4, 5]

print("Queue using two stacks:")
for elem in elements:
    queue1.enqueue(elem)
    print(f"Enqueued {elem}, front: {queue1.front()}")

while not queue1.empty():
    print(f"Dequeued: {queue1.dequeue()}")

print("\nQueue using optimized stacks:")
for elem in elements:
    queue2.enqueue(elem)
    print(f"Enqueued {elem}, front: {queue2.front()}")

while not queue2.empty():
    print(f"Dequeued: {queue2.dequeue()}")

print("\nQueue using single stack:")
for elem in elements:
    queue3.enqueue(elem)
    print(f"Enqueued {elem}, front: {queue3.front()}")

while not queue3.empty():
    print(f"Dequeued: {queue3.dequeue()}")
