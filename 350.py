s = input()
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print(f"Letters {letters}")
print(f"Digits {digits}")

