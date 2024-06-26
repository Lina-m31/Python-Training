def factorial (n):
    fact=1
    for i in range(1 , n+1):
        fact= fact * i
    return fact 


def list_factorial(n):
# return [factorial (f) for f in n]
    fact_list=[]
    for x in (n):
      fact_list.append(factorial(x))
    return fact_list

  
