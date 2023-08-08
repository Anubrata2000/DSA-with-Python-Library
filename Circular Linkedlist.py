class node:
    def __init__(self,info):
        self.info = info
        self.link = None
        
class clinkedlist:
    def __init__(self):
        self.start  = None
        
    def insert_at_beginning(self , value):
        n = node(value)
        if self.start == None:
            self.start = n
            n.link = self.start 
        else:
            p = self.start 
            self.start = n
            n.link = p
            s = p
            while(p.link != s):
                p = p.link 
            p.link = self.start 
            
    def insert_at_end(self , value):
        t = node(value)
        if self.start == None:
            self.start = t
            t.link = self.start 
        else:
            p = self.start 
            s = p
            while p.link != s:
                p = p.link
            p.link = t
            t.link = self.start
            
    def delete_start_node(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            p = self.start
            s = p
            item = s.info
            self.start = p.link
            while p.link != s:
                p = p.link
            p.link = self.start 
            del p
            return item
        
    def delete_last_node(self):
        if self.start == None:
            print("Empty linked list")
        else:
            p = self.start 
            s = p
            while p.link != s:
                prev = p
                p = p.link 
            prev.link = self.start 
            item = p.info
            del p
            return item
        
    def delete_at_specifiedpos(self,pos):
         if self.start == None:
             print("Empty Linked List")
         else:
             i = 1
             p = self.start
             while i<pos:
                 prev = p
                 p = p.link
                 i+=1
             item = p.info
             prev.link = p.link
             p.link = self.start
             del p
             return item
     
    def delete_after_specifieditem(self,item):
         if self.start == None:
             print("Empty Linked List")
         else:
             p = self.start
             while p != None and p.info != item:
                 p = p.link
             if p and p.link:
                item = p.info
                t = p.link
                p.link = t
                t.link = self.start
                del t
                return item
            
    def insert_node_specificpos(self,pos,value):
        t = node(value)
        if self.start == None:
            self.start = t
        else:
            i=1
            p = self.start
            while i < pos:
                prev = p
                p = p.link
                i+=1
            prev.link = t
            t.link = p
            
    def insert_after_specificitem(self,item,value):
        t = node(value)
        if self.start == None:
            self.start = t
        else:
            p = self.start
            while p!= None and p.info != item:
                prev = p
                p = p.link
            prev.link = t
            t.link = p  
            
    def display(self):
        p = self.start 
        while (p != None):
            print("Item : ",p.info)
            p = p.link 
            
def main():
        l = clinkedlist()
        l.insert_at_beginning(10)
        #l.display()
        l.insert_at_end(30)
       # l.display()
        l.insert_node_specificpos(2,20)
       # l.display()
        l.insert_after_specificitem(30,40)
       # l.display()
        l.insert_node_specificpos(5,50)
       # l.display()
        l.delete_start_node()
       # l.display()
        l.delete_last_node()
       #  l.display()
        l.delete_after_specifieditem(30)
       # l.display()
        l.search(10)
        l.display()
        
if __name__ == '__main__':
        main()