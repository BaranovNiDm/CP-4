a=[float(i) for i in input().split()]
Delta = float(input())
count=0

#найдеи кол-во отличающихся от минимального на Delta
for i in range(len(a)):
    if a[i]-min(a)==Delta:
        count+=1
print(count)