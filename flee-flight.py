import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h, d = [int(i) for i in input().split()]
n = int(input())

s = []
for i in range(n):
    eh, ed = [int(j) for j in input().split()]
    s += [[eh, ed]]
    
while h > 0:
    
    if len(s) == 0:
        print('fight')
        exit(1)
    
    s[0][0] -= d
    
    s2 = []
    
    for i in s:
        if i[0] > 0:
            s2.append(i)
            h -= i[1]
    
    s = s2


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("flee")
