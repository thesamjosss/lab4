s = input()
parts = s.split('*')
res = 1
for p in parts:
    res *= int(p)
print(res)

