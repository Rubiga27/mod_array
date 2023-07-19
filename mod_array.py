def mod_array(A,B):
    result=0
    for digit in A:
        result=(result*10+digit)%B
    return result
A=list(map(int,input().split()))
B=int(input())
result=mod_array(A,B)
print(result)



"""
input:1
A=[1,4,3]
B=2
output=1

input:2
A=[4,3,5,3,5,3,2]
B=47
output=20
"""
