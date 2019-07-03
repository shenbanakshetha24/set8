mu,pi=map(int,input().split())
mn=mu*pi
for i in range(0,mn+1):
 if(i**2==0):
  print("yes")
  break
else:
 print("no")
