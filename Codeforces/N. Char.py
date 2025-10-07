a = input()
if a.isupper():
    a = chr(ord(a) + 32)
else:
    a = chr(ord(a) - 32)
 
print(a)
