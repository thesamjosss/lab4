chars = [input() for _ in range(3)]

for char in chars:
    if '0' <= char <= '9':
        print("Yes")
    else:
        print("No")

