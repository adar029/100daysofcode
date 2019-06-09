"""day 2"""
def merge(arr):
    global cou
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        merge(l)
        merge(r)
        ln=len(l)
        lr=len(r)
        i=j=k=0
        while(i<ln and j<lr):
            if l[i]>r[j]:
                arr[k]=r[j]
                k=k+1
                j=j+1
                cou=cou+(ln-i)
            else:
                arr[k]=l[i]
                k=k+1
                i=i+1
        while i<ln:
            arr[k]=l[i]
            k=k+1
            i=i+1
        
        while j <lr:
            arr[k]=r[j]
            k=k+1
            j=j+1
global arr
global cou
cou=0
arr=[]
tes=int(input())
for t in range(tes):
    n=int(input())
    arr=[int(x) for x in input().split()]
    cou=0
    merge(arr)
    #print(arr)        
    print(cou)