"""
Created on Sat Jun  8 22:05:41 2019
link https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0/?track=md-arrays&batchId=144
@author: adarsha
"""
tes=int(input())
for t in range(tes):
    n,s=map(int,input().split())
    ll=[int(x) for x in input().split()]
    ss=0
    dn=0
    i=0
    j=0
    while i<n and j<n:
        if ss<s:
            ss=ss+ll[j]
            j=j+1
        elif ss==s:
            print(i+1,j)
            dn=1
            break
        elif ss>s:
            ss=ss-ll[i]
            i=i+1
        if ss==s:
            print(i+1,j)
            dn=1
            break
    if dn==0:
        print(-1)