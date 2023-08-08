class Stack:
    def __init__(self,size):
        self.list = list()
        self.top = -1
        self.size = size
        
    def is_empty(self):
        if self.top == -1:
            print("Stack is empty")
     
    def is_full(self):
         if len(self.list) == self.size :
             print("Stack is full")
     
    def size(self):
        print(self.size)

    def push(self, item):
        if not self.is_full():
            self.list.append(item)
            self.top+=1
        else:
            print("Stack is full")
        
    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            print("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            print(self.list[-1])
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack will be : ",self.list)
            
    def printempty(self):
        print(self.list)
            
            
            
st=Stack(5)
#st.printempty()
st.push(10)
st.push(20)
st.push(100)
print(st.pop())
st.display()            
        