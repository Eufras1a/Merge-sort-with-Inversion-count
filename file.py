import re, sys, time

inversion = 0

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
    global inversion

    mid = len(A)//2

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inversion += mid - i
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
    start_time = time.time()

    text = open(r'E:\Python Codes\Merge Sort\IntegerArray.txt')
    content = text.read().splitlines()
    num = []

    for line in content:
        num.append(int(line))
    text.close()

    # print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    # print(sys.getrecursionlimit())

    mergesort(num)

    sol = open(r'E:\Python Codes\Merge Sort\sort.txt', 'w')
    for item in num:
        sol.write(f'{str(item)}\n')
    sol.close()
    print(inversion)
    print("--- %s seconds ---" % (time.time() - start_time))