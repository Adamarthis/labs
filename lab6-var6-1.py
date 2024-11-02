txt = "я на парі посиджу, думаю пороблю всі варіанти з ОП."
res = ""
for i in range(0,len(txt),2):
    res += txt[i]+txt[i-1]
    res += "_"
print(res)
