  x1, y1 = int(input()), int(input())  # Ввід змінних
if x1 == 0 or y1 == 0:  # Умова
    print("Точка лежить на осі")  # Вивід в разі виконання умови
else:
    print("Точка не лежить ні на одній осі")

j = 0
xlist = [int(input()) for i in range(5)]
for k in range(len(xlist)):
    if k < len(xlist) - 1:
        if xlist[k] == xlist[k + 1]:
            j += 1
        else:
            pass
print(j)

A = [int(input()) for i in range(5)]
B = [int(input()) for j in range(5)]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(set(A) & set(B))
print(set(A).difference(B))
print(set(B).difference(A))
print(set(array2).difference(set(A)).difference((set(B))))


