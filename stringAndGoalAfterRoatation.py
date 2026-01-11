
'''
  Given a string s and a goal string goal, return true if and only if
  after rotating s, it can become equal to goal.
 '''
s = input()
goal = input()
if len(s) != len(goal):
    print(False)
else:
    temp = s + s
    if goal in temp:
        print(True)
    else:
        print(False)
        