def prime(n):
    f=0
    for i in range(2,n//2+1):
        if n%i==0:
            f=1
            break
    return f


num=int(input("Enter Starting Number"))
num1=int(input("Enter Last Number"))
print("Twin Prime Numbers Are")
for i in range(num, num1):
    if prime(i)==0 and prime(i+2)==0:
        print(i,i+2);