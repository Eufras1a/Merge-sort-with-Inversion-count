import sys 

def mergesort(A):

    if len(A) > 1:                              
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]         

        mergesort(L)
        mergesort(R)
        merge(A, L, R)

def merge(A, L, R):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        k += 1
        i += 1

    
    while j < len(R):
        A[k] = R[j]
        k += 1
        j += 1

if __name__ == "__main__":
    A = [6, 5, 4, 3, 2, 1] 
 #   print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)

    mergesort(A)
    print(A)