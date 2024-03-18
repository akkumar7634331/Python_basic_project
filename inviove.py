from mym import *
printline()
noc=input("enter customer name  : ")
pr=input("enetr product name  : ")
qu=int(input("enter quantity  : ") )
pi=int(input("enetr price  :  ") )
gst=qu*pi*18/100
amount=qu*pi+gst
printline()
print("your bill is ",amount)
printline() 
