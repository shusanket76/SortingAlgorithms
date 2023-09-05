a = [1,3,2,11,32,4,32,23,5,67,85,34,7,87,98,56,34,23]


for y in range(len(a)):
    sor = True
    for x in range(len(a)-1-y):
        if a[x]>a[x+1]:
            sor = False
            temp = a[x]
            a[x] = a[x+1]
            a[x+1] = temp
    if sor:
        break
print(a)
    