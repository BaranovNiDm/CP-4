#введите члены последовательности через пробел
a=[float(i) for i in input().split()]
Delta = float(input())
count=0

#найдем минимальный член член множества
minn=99999999999999999999999999999999999999999999
for i in range(len(a)):
    if a[i]<minn:
        minn=a[i]
    
#найдеи кол-во отличающихся от минимального на Delta
for i in range(len(a)):
    if a[i]-minn==Delta:
        count+=1
print(count)
