"""
link: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0/?track=md-arrays&batchId=144
Day 2"""
tes=int(input())
for t in range(tes):
    n=int(input())
    ll=[int(x)for x in input().split()]
    co2=0
    co1=0
    ss=sum(ll)
    for i in range(n):
        if ll[i]==2:
            co2=co2+1
        if ll[i]==1:
            co1=co1+1
    co0=n-co1-co2
    for i in range(co0):
        print(0,end=" ")
    for i in range(co1):
        print(1,end=" ")
    for i in range(co2):
        print(2,end=" ")
    print()