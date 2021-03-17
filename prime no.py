n=int(input("enter the number:"))
count=0
for i in range (1,n+1):
    if n%i==0:
        count +=1
if count==2:
 print("number is prime",n)
else:
   print("number is not a prime",n)
