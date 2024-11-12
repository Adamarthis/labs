def lab4_1(x1,y1):
    if x1 == 0 or y1 == 0:
        print(f"Точка лежить на осі, через координату {'x' if x1==0 else 'y'}")
    else:
        print("Точка не лежить ні на одній осі")

# приклади використання функцій для завдання 1
lab4_1(4,1)
lab4_1(0,2)
lab4_1(3,0)



def lab4_2(xlist):
    j = 0
    for k in range(len(xlist)):
        if k < len(xlist) - 1:
            if xlist[k] == xlist[k + 1]:
                j += 1
            else:
                pass
    return j

# використання для 2 завдання
print(f"Результат 2 функкції: {lab4_2([int(input()) for i in range(5)])}")



def lab4_3(A,B):
    array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Перетин",set(A) & set(B))
    print("Різниця 1",set(A).difference(B))
    print("Різниця 2",set(B).difference(A))
    print("Цифри яких немає",set(array2).difference(set(A)).difference((set(B))))

# приклад використання функції для 3 задачі
lab4_3([int(input()) for i in range(5)],[int(input()) for j in range(5)])
