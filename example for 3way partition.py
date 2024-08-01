def element(A,n):
    i=1
    j=n-1
    k=0
    x=A[0]
    while i<=j:
        if A[i]<x:
            A[i],A[k]=A[k],A[i]
            i=i+1
            k=k+1
        elif A[i]>x:
            A[i],A[j]=A[j],A[i]
            j=j-1
        else:
            i=i+1
    return A
A=[5,6,5,1,5,8,3]
n=len(A)
print(element(A,n))
