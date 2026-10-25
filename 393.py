n1 = input().strip()
k1, m1 = map(int, input().split())

n2 = input().strip()
k2, m2 = map(int, input().split())

n3 = input().strip()
k3, m3 = map(int, input().split())

tests = [(n1, k1, m1), (n2, k2, m2), (n3, k3, m3)]

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for n_str, k, m in tests:
    dec_val = int(n_str, k)

    if dec_val == 0:
        print(0)
    else:
        is_negative = dec_val < 0
        val = abs(dec_val)
        res = ""
        while val > 0:
            res = digits[val % m] + res
            val //= m
        if is_negative:
            res = "-" + res
        print(res)

