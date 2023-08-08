#Tower of Hanoi
def toh(n,b,aux,end):
    if n == 1:
        print("Move disk",b,"to",end)
        return
    else:
        toh(n-1,b,end,aux)
        print("Move disk",b,"to",end)
        toh(n-1,aux,b,end)
toh(4,'a','b','c')
