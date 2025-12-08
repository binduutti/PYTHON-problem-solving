'''Write a java program to count total digits in a number.
    Example:
    Input: num=12345
    Output: Total digits=5'''


n = int(input("Enter number: "))
count =0
while n>0:
    count += 1 
    n = n//10
print(f"count of digits in number: {count}")
    