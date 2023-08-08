# import linklist
class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class stack:
    def __init__(self):
        self.start=None
        self.top=None
    def push(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
            self.top=n
        else:
            self.top.link=n
            self.top=n
    def pop(self):
        if self.start==None:
            print("stack is empty")
        elif self.start==self.top:
            p=self.top
            item=self.top.info
            self.start=None
            self.top=None
            del p
            return item
        else:
            p=self.start
            while p.link!=self.top:
                p=p.link
            p.link=None
            q=self.top
            self.top=p
            item=q.info
            del q
            return item
    def display(self):
        if self.top==None:
            print("stack is empty")
        else:
            temp=self.start
            while temp!=self.top:
                print(temp.info,end=" ")
                temp=temp.link
            print(temp.info)
                


ob=stack()
ob.push(40)
ob.push(20)
ob.push(70)
ob.push(60)
ob.push(6)
ob.display()
print(ob.pop())
print(ob.pop())
ob.display()