s1=input()
s2=input()
s3=input()
s4=input()

s=''
for i in range(0,len(s3)):
    k=s1.find(s3[i])
    s=s+s2[k]
print(s)
s=''
for i in range(0,len(s4)):
    k=s2.find(s4[i])
    s=s+s1[k]
print(s)