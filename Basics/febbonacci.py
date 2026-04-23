#Febbonacci : it is a series of number where each number is the sum of the two number before it. for example
def febonacci(num):
    series = []
    a = 0
    b = 1
    series.append(a)
    series.append(b)
    for i in range(num-2):
        c = a+b
        series.append(c)
        a = b
        b = c
    return series
num = 5
print(febonacci(num))

#question: print the febbonacci series for the given value.
#for example input  = 5 so output should be 0,1,2,3,5
#approach : I take 2 inputs a and b assign value to a,b = 0,1 so now first I insert that two element inside the list then i go through the range
# update c as a+b and add c inside list after update values of a and b .

def febonacciUsingRec(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return (febonacci(num-1)+febonacci(num-2))
n = 20
for i in range(n):
    print(febonacci(i))