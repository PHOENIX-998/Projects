message = "C"

l = list(bin(ord(message))[2:])
temp = l[0]
count = 0
out = []

for i in l:
    if temp != i:
        out.append((temp,count))
        temp = i
        count = 1
    else:
        count += 1
out.append((temp, count))

# Unary encoding print
for t, c in out:
    if t == "1":
        print("0 ", end="")   # header for '1' sequence
    elif t == "0":
        print("00 ", end="")  # header for '0' sequence
    print("0" * c, end=" ")   # c zeros