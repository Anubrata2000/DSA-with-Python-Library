class graph:
    
    def __init__(self,row,col):
        self.adj=[]
        self.row=row
        self.column=col
        for row in range(6):
            a=[]
            for col in range(6):
        #a.append(f"{row}{column}")
                a.append(0)
            self.adj.append(a)
    
    
    def createadjmatrix(self):
                l=[(0,1),(0,2),(1,2),(2,4),(3,5),(4,5)]
                for i in l:
                    self.adj[i[0]][i[1]]=1
    
    
    def display(self):
                for row in range(6):
                    for col in range(6):
                        print(self.adj[row][col],end=' ')
                    print()


ob=graph(6,6)
ob.createadjmatrix()
ob.display()