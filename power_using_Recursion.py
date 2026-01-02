'''Calculate the power of a number using recursion.'''
a,b = map(int,input().split())

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

print(power(a,b))