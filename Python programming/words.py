dict = {}
s=''
with open('text.txt') as inf:
    for line in inf:
        line=line.strip()
        s = s+line+' '
s1 = s.lower()
lst = s1.split(' ')

for word in lst:
    if word in dict:
        dict[word] = dict[word] + 1
    else:
        dict.update([(word, 1)])

for key, value in dict.items():
    print(key, value)
    #key=слово, value=число
