mu,pi=map(int,input().split())
mn=mu*pi
for j in range(0,mn+1):
 if(j**2==0):
  print("yes")
  break
else:
 print("no")
