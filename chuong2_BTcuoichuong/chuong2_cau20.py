import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def f(m, n):
    gcd = math.gcd(m, n)
    if gcd < 2:  
        return 0

    max_prime = 0
   
    for i in range(2, gcd + 1):
        if gcd % i == 0 and is_prime(i):
            if i > max_prime:
                max_prime = i
    return max_prime