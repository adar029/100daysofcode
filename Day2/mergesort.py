"""day 2"""
def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        merge(l)
        merge(r)

        i=j=k=0

        while(i<len(l) and j<len(r)):
            if l[i]>r[j]:
                arr[k]=r[j]
                k=k+1
                j=j+1
            else:
                arr[k]=l[i]
                k=k+1
                i=i+1
        while i<len(l):
            arr[k]=l[i]
            k=k+1
            i=i+1
        
        while j <len(r):
            arr[k]=r[j]
            k=k+1
            j=j+1
global arr
arr=[]
arr=[int(x) for x in input().split()]
merge(arr)
print(arr)        