from Basics.primes import primes

def printNPime(n):
    series = []
    i = 2
    while len(series) < n:
        if primes(i):
            series.append(i)
        i = i + 1
    return series


n = 10
print(printNPime(n))


#Breaking logic into reusable functions” is basically about not writing the same code again and again,
# and instead putting that logic inside a function so you can reuse it anywhere.

# for example i did not write a entire code i used primes so it can reuse the existing code


#instead of writing a large code make it smaller and reusable and readable
