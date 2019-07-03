ni=int(input())
if(ni>1):
 for i in range(2,ni):
  if(ni%i==0):
   print("yes")
   break
 else:
  print("no")
