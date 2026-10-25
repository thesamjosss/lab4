text = input()

max_len = 0
current_len = 0

for char in text:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 0

if current_len > max_len:
    max_len = current_len

k = max_len

res = []
for char in text:
    if 'a' <= char <= 'z':
        new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        res.append(new_char)
    elif 'A' <= char <= 'Z':
        new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        res.append(new_char)
    else:
        res.append(char)

print(''.join(res))

