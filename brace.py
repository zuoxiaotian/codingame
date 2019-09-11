s="([{"
m=")]}"
f="FALSE"
b=[]
for i in input():
 if i in s:b+=[i]
 if i in m:
  if len(b)==0 or not b.pop()==s[m.find(i)]:print(f);exit(1)
print("TRUE"if len(b)==0else f)
