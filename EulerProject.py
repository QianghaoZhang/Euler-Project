#q1 calculate the sum of numbers that is divided by 3 or 5 integerly 
def fin(n):
    list = []
    for num in range(n):
        if num % 3 ==0 or num %5==0:
             list.append(num)
    return list
    
   
 #q2, figure out the even fibonacii number
 def fin2(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a , b = b, a + b
 def even_fibo(n):
    list=[]
    for num in fin2(n):
        if num % 2 ==0:
            list.append(num)
    return list
 
 
 #  Q3 finding the largest prime factor
 def prime(n):
    pfactors = []
    if n==1:
        pfactors.append(1) 
    for num in range(2,n):
        if n%num ==0:
            pfactors.append(num)
    return max(pfactors)
        
