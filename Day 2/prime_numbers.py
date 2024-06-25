import Prime 

n=int(input("Please inter a number:"))
x=0
for i in range (1,n):
  if Prime.is_prime(i) :
    x=x+1 

print (x)
 