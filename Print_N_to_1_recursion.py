'''
Write a recursive function to print numbers from N to 1.
e.g., if N = 3, the output should be:
3
2
1
'''

def printt(n):
    if(n<1):
        return
    print(n)
    printt(n-1)

n=int(input("Enter number: "))
printt(n)