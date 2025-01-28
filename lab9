import random as rn


def task_1(clist):
    counter = 0
    if clist:
        for i in clist:
            if i ** 2 in clist:
                counter += 1
        return f"Елементів з квадратом в масиві: {counter}"
    else:
        return "Неможливо виконати завдання, список порожній"


def task_2(clist):
    new_list = [i for k in range(0, len(clist), 5) for i in reversed(clist[k:k+5:])]
    if new_list:
        return f"Відредагований масив: {new_list}"
    else:
        return "Неможливо виконати завдання, список порожній"

lists = []
for k in range(5):
    lists.append([rn.randint(0, 100) for i in range(rn.randint(0, 100))])
for num, i in enumerate(lists, 1):
    print(f"Масив {num}: {i}")

print("\n5 прикладів виконання 1 завдання")
for i in lists:
    print(task_1(i))

print("\n5 прикладів виконання 2 завдання")
for i in lists:
    print(task_2(i))

