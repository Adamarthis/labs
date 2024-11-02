txt="123456789"
result = ""
for i in range(0, len(txt), 3):
    result+=txt[i:i+3][::-1]
print(result)
