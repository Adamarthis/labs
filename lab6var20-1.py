txt = "Така цікава лекція, що аж ноутбук заснув."
latin = [chr(j) for j in range(65, 91)] + [chr(j) for j in range(97, 123)]
kiril = [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(1040, 1072)]
only_latin = False
only_kiril = False
for i in txt:
    if i in latin:
        only_latin = True
    elif i in kiril:
        only_kiril = True
if only_latin and only_kiril:
    print("Тут і кирилиця і латинь")
elif only_latin and not only_kiril:
    print("Тут лише латинь")
else:
    print("Тут лише кирилиця")


