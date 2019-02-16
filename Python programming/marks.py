with open('text.txt') as inf:
    sum1=0
    sum2=0
    sum3=0
    n=0
    for line in inf:
        n=n+1
        sum=0
        line=line.strip()
        lst=line.split(';')
        del lst[0]
        lst1=[int(i) for i in lst]
        sum=lst1[0]+lst1[1]+lst1[2]
        print(sum/3)
        sum1=sum1+lst1[0]
        sum2 = sum2 + lst1[1]
        sum3 = sum3 + lst1[2]
    print(sum1/n, sum2/n, sum3/n)