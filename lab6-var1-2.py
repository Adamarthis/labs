txt = "<kf ,kf Бла бла Ааааа"
golosni = "EeYyUuIiOoAaJjУуЕеЇїІіАаОоЄєЯяИиЮю"
count = 0
txt = list(txt.split())
for i in txt:
    if i[0] in golosni:
        count+=1
print(count)
