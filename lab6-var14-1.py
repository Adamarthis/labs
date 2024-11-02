txt= "івтоіватоів"
nums="0123456789"
is_there_a_numbers = False
for i in txt:
    if i in nums:
        is_there_a_numbers = True
if is_there_a_numbers:
    print("Тут є числа")
else:
    print("Тут немає чисел")
