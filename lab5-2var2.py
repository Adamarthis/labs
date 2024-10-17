A = int(input()[::-1])
B = int(input())
counter = 0
for i in range(A):
    if i % B == 0:
        counter += 1
print(counter)
