txt = "f  f f.  f"
result=""
for i in range(0, len(txt)):
    if txt[i]==(txt[i-1])==" ":
        pass
    else:
        result+=str(txt[i])
print(result)
