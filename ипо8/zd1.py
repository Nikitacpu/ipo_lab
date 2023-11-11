n=int(input("Введите число: "))
prost=list(range(n+1))
prost[1]=0
for i in range(n+1):
    if prost[i]!=0:
        for j in range(i+i,n+1,i):
            prost[j]=0
prost_set = set(prost)# Преобразование в множество
prost_set.discard(0)# Удаление 0
print(prost_set)# Вывод множества
