def is_prime(n: int):

    if n > 0 :
       for i in range (2 , 12) :
           prime=True
           
           if (n == i):
               continue
           elif ( n%i == 0) :
               prime = False
               break
           else:
               prime = True
    else: 
        return False
    return prime
       
