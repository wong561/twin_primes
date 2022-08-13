def prime(n):
    tp=[]
    for i in range(2,n//2+1):
        if n%i==0:
            tp.append(i)
            f=1
            print("here",tp)
            break
    return tp


num=int(input("Enter Starting Number"))
num1=int(input("Enter Last Number"))
print("Twin Prime Numbers Are")

for i in range(num, num1):
    
    if prime(i)==0 and prime(i+2)==0:
    #return
    
        #tp.append(i)
        print(i,i+2);
        #print(tp)
                 
#tp.append(i)
#print(tp)