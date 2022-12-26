n=int(input())
a=1
for i in range(2,n):
    if n%i==0:
        a=a+1
if a==1:
 print('prime')
else:
     print('not prime')