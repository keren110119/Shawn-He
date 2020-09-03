line = input()
a = line.split(',')[0]
b = line.split(',')[1]

area = []
for h in b:
    length = 0
    for i in range(len(b)):
        if h <= b[i]:
            length = length+a[i]
            area.append(h*lenght)
print(max(area))