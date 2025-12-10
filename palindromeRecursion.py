'''
write a program to check whether a given string is a palindrome using recursion.
example:
Input: "madam"
Output: "Palindrome"
'''
def rev(s):
    if not s:
        return ""
    return s[-1]+rev(s[:-1])
    

s=input("Enter string: ").strip()
copy = s
reverse = rev(s)
print("Palindrome" if copy== reverse else "Not palindrome")