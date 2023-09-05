a = [54,34,23,12,32,34,53,23,35,46]

def quicksort(a, start, end):
    pivot = a[start]
    l=start+1
    while l<=end:
        while l<=end and  a[l]<=pivot:
            l+=1
        while a[end]>pivot:
            end-=1
        if l<end:
            temp = a[l]
            a[l] = a[end]
            a[end] = temp
    temp = a[end]
    a[end] = pivot
    a[start] = temp
    return end

def partation(a, start, end):
    if start<end:
        pi = quicksort(a,start,end)
        partation(a, start,pi-1)
        partation(a, pi+1, end)

partation(a, 0, len(a)-1)
print(a)