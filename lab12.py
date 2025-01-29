arr2D =[]
is_ok = True
class IncorrectRowLen(Exception):
    pass
def kill():
    print("Помилка, неправильні числа (-1000<x<1000)")
    exit()
while is_ok:
    try:
        with open("arraydata.txt") as file:
            correct_len = len(list(file.readline().split()))
            file.seek(0)
            for line in file:
                row = [int(x) for x in line.split()]
                if len(row) != correct_len:
                    raise IncorrectRowLen()
                arr2D.append(row)
            is_ok = False
    except FileNotFoundError:
        print("Помилка")
        exit()
    except ValueError:
        print("Помилка")
        exit()
    except IncorrectRowLen:
        print("Помилка, нерівна довжина рядків.")
        exit()
m = len(arr2D[0])

with open("result.txt", "w") as file:
    file.write("2D ARRAY:\n")
    for i in arr2D:
        for k in i:
            kill() if k > 1000 or k < -1000 else file.write(str(k) + " ")
        file.write("\n")
with open("result.txt", "a") as file:
    file.write("\nTask 1:\n")
    for num, i in enumerate(arr2D, 2):
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
        file.write(f"   {num} row:\nPositive: {round((positive*100)/m,2)}%\nNegative: {round((negative*100)/m,2)}%\nZeros: {round((zeros*100)/m, 2)}%")
        file.write("\n")
for i in arr2D:
    for k in range(1,len(i), 2):
        i[k-1], i[k] = i[k], i[k-1]
with open("result.txt", "a") as file:
    file.write("\nTask 2:\n")
    file.write("EDITED ARRAY:\n")
    for i in arr2D:
        for k in i:
            file.write(str(k) + " ")
        file.write("\n")

