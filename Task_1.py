# 1st program.
print(5 * 9 ** 0.5)

#2nd program.
if 9.99 > 9.98 and 1000 != 1000.1:
    print(True)

# 3rd program.
a = (2 * 2 + 2)
print(a)
b = (2 * (2 + 2))
print(b)
if a == b:
    print(True)
else:
    print(False)

# 4th program.
string = '123.456'
gene = [i for i in string if i == '4']
print(*gene)
add = float(string)
add2 = add * 10
print(int(add2) % 10)
