a = [54,34,23,12,32,34,53,23,35,46]

l = 0 
while l<len(a)-1:
    if a[l]>a[l+1]:
        j=l
        pivot = a[l+1]
        while j>=0 and  a[j]>=pivot:
            j-=1
        temp = a[j+1]
        a[j+1]=pivot
        a[l+1] = temp
    l+=1

print(a)