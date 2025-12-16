'''
write a program to reverse a list of boolean values.
example: input: [true, false, true, false]
         output: [false, true, false, true] 
'''
listt = list(map(lambda x: bool(int(x)), input().split()))

revlist = []
for i in range(len(listt)-1, -1, -1):
    revlist.append(listt[i])

print(revlist)
