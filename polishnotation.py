
list=input("Enter the infix expression:").split(" ")

paren=[]
opr=[]
operand=[]

for i in list:
    if i=="(":
        paren.append(i)
        
    elif i==")":
       paren.append(i)
             
    elif i=="+" or i=="-" or i=="/" or i=="*" or i=="^" or i=="%":
           opr.append(i)
                     
    elif ord(i)>=65 or ord(i)<=90 or ord(i)>=97 or ord(i)<=122 or i.isnumeric():
        operand.append(i)
        
print(paren) 
print(opr)
print(operand)
