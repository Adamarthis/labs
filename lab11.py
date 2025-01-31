import random as rn
is_ok = False

# # - log

while not is_ok:
    try:
        l = int(input("Введіть глибину:"))
        m = int(input("Введіть рядки:"))
        n = int(input("Введіть стовпці:"))
        is_ok = True
    except ValueError:
        print("Помилкове значення")

arr = []

for i in range(m):
    for g in range(n):
        arr.extend([[[rn.randint(0,3) if rn.randint(0,100)>25 else rn.randint(4,7) for k in range(l) ], i, g]])

# for i in arr:
#     print(f"({i[1]},{i[2]}), зміст: {i[0]}")

count = 0
for i in arr:
    if 7 in i[0] and 3 not in i[0]:
        # print(f"Координати стовпця без води і з золотом:({i[1]},{i[2]}), зміст: {i[0]}")
        count += 1

print("Кількість стовпців без води і з золотом: ", count)

