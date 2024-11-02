txt = "я на парі посиджу, думаю пороблю всі варіанти з ОG."
count = 0
txt = list(txt.split())
print(txt)
for i in txt:
    if i[0].isupper() and i[1::].islower():
        count+=1
print(count)
