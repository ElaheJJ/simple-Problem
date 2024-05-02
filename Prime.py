#prime function
def TestAval(Number):
    aval =True
    for i in range(2,Number):
        if Number%i==0:
            aval=False
            break
    return aval           
    
#print Prime number 1 to 1000
for i  in range(1,1001):
    if TestAval(i)==True:
        print(i)
