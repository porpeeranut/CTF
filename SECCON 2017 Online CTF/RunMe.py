# https://cboard.cprogramming.com/c-programming/67989-highest-fibonacci-number-ever-calculated.html
def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f
 
def pow(A, n):
    if n == 1:     return A
    if n & 1 == 0: return pow(mul(A, A), n/2)
    else:          return mul(A, pow(mul(A, A), (n-1)/2))
 
def fib(n):
    if n < 2: return n
    return pow((1,1,0), n-1)[0]
 
print "SECCON{" + str(fib(11011))[:32] + "}"