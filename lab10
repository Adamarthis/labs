import random as rn
m = rn.randint(1, 7)
n = rn.randint(1, 7)
arr2D = [[rn.randint(-1000, 1000) for k in range(n)] for i in range(m)]

print(f"m (рядків):{m}\nn (стовпців):{n}\nДвовимірний масив:")

for i in arr2D:
    print(i)

for i in arr2D:
    negative = 0
    positive = 0
    zeros = 0
    for k in i:
        if k>0:
            positive += 1
        elif k<0:
            negative += 1
        else:
            zeros += 1
    print(f"Відсоток позитивних чисел: {round(positive*100/n, 2)}%\nВідсоток від'ємних чисел:{round(negative*100/n, 2)}%\nВідсоток нульових чисел:{round(zeros*100/n, 2)}%\n")

for i in arr2D:
    for k in range(1,len(i), 2):
        i[k-1], i[k] = i[k], i[k-1]

for i in arr2D:
    print(i)



