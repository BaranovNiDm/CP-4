print("введите размерность массива")
lenn=int(input())
print("введите элементы массива через пробел(колличество элементов равно размерности массива)1")
a=[float(i) for i in input().split()]
print(*a)
maxx=0
k=0
for i in range(0,lenn):
    if (a[i])>maxx:
        maxx=a[i]
        num=k
    k+=1
for i in range(num+1,lenn):
    a[i]=0
print(a)
