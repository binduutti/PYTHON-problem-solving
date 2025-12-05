'''
Write a Python program to print the following continuous number triangle pattern up to n rows.
Input Number: 5
Expected Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n = int(input("Enter number: "))
val=1
for i in range(1, n + 1):

    for j in range(1, i + 1):
        
        print(val, end=" ")
        val +=1
    
    print()
