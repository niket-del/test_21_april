import math
def primes(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = 5
print(primes(n))


# prime check weather the number is prime or not
# prime are those numbers which can be only  divide by itself.
