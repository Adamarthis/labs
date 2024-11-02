txt="текст сюда вставиш"
txt = list(txt.split())
counter=0
for i in txt:
    if "'" in i:
        counter+=1
print(counter)
