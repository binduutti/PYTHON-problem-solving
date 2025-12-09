'''
Write a recursive function to print numbers from 1 to N.
e.g., if N = 3, the output should be:
1
2
3
'''
def printt(n):
    if(n<1):
        return
    printt(n-1)
    print(n)
printt(int(input("Enter Number: ")))