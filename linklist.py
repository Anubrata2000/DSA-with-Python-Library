class node:
    def __init__(self,value):
        self.info=value
        self.link=None
class LinearLinkedList:
    def __init__(self):
        self.start=None
    def insert_at_beginning(self,value):
        n1=node(value)
        n1.link=self.start
        self.start=n1
    def inser_at_end(self,value):
        t=node(value)
        temp=self.start
        while temp.link!=None:
            temp=temp.link
        temp.link=t
    def delete_at_start(self):
        temp=self.start
        self.start=temp.link
        item=temp.info
        del temp
        return item
    def delete_last_node(self):
        temp=self.start
        while temp.link!=None:
            previous=temp
            temp=temp.link
        item=temp.info
        del temp
        previous.link=None
        return item
    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info,end=" ")
            temp=temp.link
    def insert_at_specified_pos(self,value,pos):
        i=1
        t=node(value)
        temp=self.start
        while i== pos-1:
            previous=temp
            temp=temp.link
            i+=1
        previous.link=t
        t.link=temp
    def insert_after_specified_item(self,value,item):
        temp=self.start
        n=node(value)
        while temp.link!=None and temp.info!=item:           
            temp=temp.link
        n.link=temp.link
        temp.link=n
    def delete_at_specified_pos(self,pos):
        temp=self.start
        i=1
        while i!=pos:
            previous=temp
            temp=temp.link
            i+=1
        item=temp.info        
        previous.link=temp.link
        del temp
        return item
    def delete_specified_item(self,item):
        temp=self.start
        while temp.link!=None and temp.info!=item:
            previous=temp
            temp=temp.link
        previous.link=temp.link
        item=temp.info
        del temp
        return item
    


class CircularLinkedList:
    def __init__(self):
        self.start=None
    def insert_at_beginning(self,value):
        n=node(value)
        if self.start==None:
            self.start=n
            n.link=self.start
        else:
            p=self.start
            self.start=n
            n.link=p
            s=p
            while p.link!=s:
                p=p.link
            p.link=self.start
    def insert_at_end(self,value):
        t=node(value)
        temp=self.start
        s=temp
        while temp.link!=s:
            temp=temp.link
        temp.link=t
        t.link=s
    def delete_start(self):
        temp=self.start
        self.start=temp.link
        s=temp
        while temp.link!=s:
            temp=temp.link
        temp.link=self.start
        del s
    def delete_end(self):
        temp=self.start
        s=temp
        while temp.link!=s:
            previous=temp
            temp=temp.link
        previous.link=s
        item=temp.info
        del temp
        return item
    def display(self):
        temp=self.start
        while temp.link!=self.start:

            print(temp.info,end=" ")
            temp=temp.link
        print(temp.info)
    def insert_at_specified_pos(self,value,pos):
        n=node(value)
        temp=self.start
        i=1
        while i!=pos-1:
            previous=temp
            temp=temp.link
            i+=1
        n.link=temp.link
        temp.link=n
    def insert_after_specified_item(self,item,value):
        temp=self.start
        n=node(value)
        while temp.link!=self.start and temp.info!=item:            
            temp=temp.link
        n.link=temp.link
        temp.link=n
    def delete_at_specified_pos(self,pos):
        temp=self.start
        i=1
        while i!=pos:
            previous=temp
            temp=temp.link
            i+=1
        item=temp.info
        previous.link=temp.link
        del temp
        return item     
    def delete_specified_item(self,item):
        temp=self.start
        while temp.link!=self.start and temp.info!=item:
            previous=temp
            temp=temp.link
        previous.link=temp.link
        item=temp.info
        del temp
        return item        




        
        