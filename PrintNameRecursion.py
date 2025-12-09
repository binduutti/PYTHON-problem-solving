'''
Write a recursive function to print your name N times.
e.g., if N = 3, the output should be:
SAI BINDU
SAI BINDU
SAI BINDU
'''

def printt(n):
    if(n<1):
        return
    print("SAI BINDU")
    printt(n-1)

n = int(input())
printt(n)
