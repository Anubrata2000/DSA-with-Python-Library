class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.key = value
        
class BST:
    def __init__(self):
        self.root = None
        
    def createbst(self,l):
        for item in l:
            n = node(item)
            if self.root == None:
                self.root = n
            else:
                temp = self.root 
                #par = None
                while(temp != None):
                    if item < temp.key:
                        par = temp
                        temp = temp.left
                    else:
                        par = temp
                        temp = temp.right
                
                if item < par.key:
                    par.left = n
                else:
                    par.right = n
                    
    def preorder(self,T):
        if T!= None:
            print(T.key,end=" ")
            self.preorder(T.left)
            self.preorder(T.right)

    def inorder(self,T):
        if T!= None:
            self.inorder(T.left)
            print(T.key,end=" ")
            self.inorder(T.right)

    def postorder(self,T):
        if T!= None:
            self.postorder(T.left)
            self.postorder(T.right)
            print(T.key,end=" ")   
            
    def height(self,T):
        if T == None:
            return 0
        else:
            return max(self.height(T.left),self.height(T.right)) + 1
        
    def search(self,item):
        par = None
        temp = self.root
        while temp != None:
            if item == temp.key:
                print("Item found")
                return temp,par
            else:
                if item < temp.key:
                    par = temp
                    temp = temp.left
                else:
                    par = temp
                    temp = temp.right
        print("Item not found")
        
    def delete(self, value):
        node, parent = self.search(value)
        if node == None:
            return False
        elif node.left == None and node.right == None:
           if parent.left == node:
                parent.left = None
           else:
                parent.right = None
                del node
        elif node.left == None:
            if parent == None:
                self.root = node.right
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
                del node
        elif node.right == None:
            if parent == None:
                self.root = node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
                del node
                
        else:
            successor_parent = node
            successor = node.right
            while successor.left != None:
                successor_parent = successor
                successor = successor.left
            print("Inorder successor: ",successor.key)
            key1 = successor.key
            if successor_parent.left == successor:
                successor_parent.left = None
            else:
                successor_parent.right = None
            del successor.key
            node.key = key1

        

        
        
bst = BST()
#values = [100,50,670]
values = [0,10,4,9,6]
root = bst.createbst(values)
print("Preorder traversal:",end=" ")
bst.preorder(bst.root)
print("\nInorder traversal:",end=" ")
bst.inorder(bst.root)
print("\nPostorder traversal:",end=" ")
bst.postorder(bst.root)
print("\nHeight of tree: ",bst.height(bst.root))
item = int(input("Enter an item to be searched: "))
print(bst.search(item))
bst.delete(0)
bst.inorder(bst.root)








'''class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None
        
    def create_bst(self, l):
        """
        Recursive function to create a binary search tree from a list of values.
        """
        if len(l) == 0:
            return None
        mid = len(l) // 2
        root = Node(l[mid])
        root.left = self.create_bst(l[:mid])
        root.right = self.create_bst(l[mid+1:])
        return root
    
    def traverse_bst(self, root, order):
        """
        Function to traverse a binary search tree in the specified order (preorder, inorder, or postorder).
        """
        if root is not None:
            if order == 'preorder':
                print(root.value)
            self.traverse_bst(root.left, order)
            if order == 'inorder':
                print(root.value)
            self.traverse_bst(root.right, order)
            if order == 'postorder':
                print(root.value)'''