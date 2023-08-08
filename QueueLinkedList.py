class node:
    def __init__(self,value):
        self.info=value
        self.link=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        n=node(value)
        if self.front==None:
            self.front=n
            self.rear=n
        else:
            p=self.rear
            p.link=n
            self.rear=n
    def dequeue(self):
        if self.front==None and self.rear==None:
            print("queue is empty")
        elif self.front==self.rear:
            q=self.front
            item=q.info
            del q
            self.front=None
            self.rear=None
            return item
        else:
            p=self.front
            item=p.info
            self.front=p.link
            del p
            return item
    def display(self):
        temp=self.front
        while temp!=self.rear:
            print(temp.info)
            temp=temp.link
        print(temp.info)


ob=queue()
ob.enqueue(30)
ob.enqueue(50)
ob.dequeue()
ob.display()