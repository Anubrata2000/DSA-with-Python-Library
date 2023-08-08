class node:
    def __init__(self,info):
        self.info = info
        self.link = None
        
class slinkedlist:
    def __init__(self):
        self.start = None
        
    def insert_at_beginning(self,value):
        t = node(value)
        if self.start == None:
            self.start = t
        else:
            t.link = self.start
            self.start = t
            
    def insert_at_end(self,value):
        t = node(value)
        if self.start == None:
            self.start = t
        else:
            p = self.start
            while (p.link != None):
                p=p.link
            p.link = t   
            
    def delete_start_node(self):
        if self.start == None:
            print("Empty linked list.")
        else:
            p = self.start
            self.start = p.link
            item = p.info
            del p
            return item
            
    def delete_last_node(self):
        if self.start == None:
            print("Empty linked list.")
        else:
            p = self.start
            while(p.link != None):
                prev = p
                p=p.link 
            prev.link = None
            item = p.info
            del p
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
               p.link = t.link
               del t
               return item        
                    
    def search(self,item):
        p = self.start 
        while (p != None):
            if (p.info == item):
                print("Item found")  
                p = p.link
                break
            else:
                print("Item not found")
                p = p.link
                
    def display(self):
        p = self.start 
        while (p != None):
            print("Item : ",p.info)
            p = p.link   
            
def main():
        l = slinkedlist()
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
        