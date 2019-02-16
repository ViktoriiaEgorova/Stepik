with open('text.txt') as inf:
    s = inf.readline()

#s=input()
sym=s[0]
k=0
for i in range(1,len(s)):
    if s[i].isdigit():
        if k==0:
            k=int(s[i])
        else:
            k=k*10+int(s[i])
    else:#прочитали подстроку
        print(sym*k, end='')
        sym=s[i]
        k=0
print(sym*k, end='')