class Node:
    def __init__(self,data):
        self.item = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.count += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped_item = self.top.item
            self.top = self.top.next
            self.count -= 1
            return popped_item
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.top.item
        
    def display(self):
        current = self.top 
        if current is None:
            print("Stack is empty")
            return
        while current:
            print(current.item,end=" ")   
            current = current.next
        print("None") 


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print("Stack after pushing elements:",end=" ")
stack.display()
print("popped item:",stack.pop())
print("Stack after popping an item:",end=" ")
stack.display()
print("peeked item:",stack.peek())