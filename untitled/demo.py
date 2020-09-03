line = input()
a = line.split(',[')[0]
b = line.split('],')[1]
L = []
H = []
for i in a:
    if (i !='[' and i!=']') and i !=',':
        L.append(i)
for m in b:
    if (m !='[' and m!=']') and m !=',':
        H.append(m)
area = []
for h in range(len(H)):
    length = 0
    for i in range(len(H)):
        if H[h] <= H[i]:
            length = int(length)+int(L[i])

        if H[h] > H[i]:
            if h > i:
                length = 0
            else:
                break
        area.append(int(H[h]) * length)

print(max(area))
