def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]     
            j = j - 1           
        A[j + 1] = key
        printStep(A, i)
    return A

def insertion_sort_recur(A, n):
    if n == 1: return
    insertion_sort_recur(A, n - 1)
    key = A[n - 1]
    j = n - 2
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j = j - 1
        A[j + 1] = key

def printStep(arr, val):
    print("  %2d Step =  " % val, end='')
    print(arr)

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data.copy())

print("Insertion", insertion_sort(data.copy()))
print("Original : ", data)
insertion_sort_recur(data, len(data))
print("Insertion_Recur", data)