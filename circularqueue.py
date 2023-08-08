class circularqueue:
    def __init__(self,s):
        self.front=-1
        self.rear=-1
        self.size=s
        self.qu=[0 for i in range(s)]
    def enqueue(self,item):
        if self.front==(self.rear+1)%self.size:
            print("queue is full")
            return
        
        self.rear=(self.rear+1)%self.size
        self.qu[self.rear]=item
        print("rear is",self.rear)
        #print(item)
        if self.front==-1:
            self.front=0
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
            return
        else:
            item=self.qu[self.front]
            #self.qu.pop(self.front)
            if self.front==self.rear:
                self.rear=-1
                self.front=-1
            
            else:
                self.front=(self.front+1)%self.size
                print("front is",self.front)
            return item
    def display(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
            return
        else:
           i=self.front
           while i!=self.rear:
               print(self.qu[i])
               i=(i+1)%self.size 
        print(self.qu[i])

ob=circularqueue(3)
ob.enqueue(5)
ob.enqueue(78)
ob.enqueue(89)
ob.dequeue()
ob.enqueue(34)
ob.display()
        