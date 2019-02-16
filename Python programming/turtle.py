n=int(input())
x=0
y=0
for i in range(0,n):
    s=input().split()
    if s[0]=='север':
        y=y+int(s[1])
    if s[0] == 'юг':
        y = y - int(s[1])
    if s[0]=='восток':
        x=x+int(s[1])
    if s[0]=='запад':
        x=x-int(s[1])

print(x, y)