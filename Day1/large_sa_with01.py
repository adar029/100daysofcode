"""
Created on Sat Jun  8 19:44:47 2019
need optimisation
link :https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1/?track=md-arrays&batchId=144
"""
def maxLen(n, lis):
    #code here
    cou1=0
    cou=0
    for i in range(n):
        if lis[i]==0:
            lis[i]=-1
            cou=cou+1
    s=sum(lis)
    cou1=n-cou
    max=0
    for i in range(n):
        for j in range(i,n):
            a1=lis[i:j+1]
            if sum(a1)==0:
                if len(a1)>max:
                    max=len(a1)
    return max
