def bubble_sort(A):
    print("시작 : ", A)
    n_swap = 0
    n = len(A)
    for i in range(n - 1):
        swap = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swap = True
                n_swap += 1
        printStep(A, i)
        if swap == False:
            break
    print("결과 : :", A)
    print("연산 횟수 : ", n_swap)


def selection_sort(A):
    print("시작 : ", A)
    n = len(A)
    n_swap = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                n_swap += 1
        printStep(A, i)
    print("결과 : ", A)
    print("연산 횟수 : ", n_swap)

def quick_sort(A):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = A[(low + high) // 2]
        while low <= high:
            while A[low] < pivot:
                low += 1
            while A[high] > pivot:
                high -= 1
            if low <= high:
                A[low], A[high] = A[high], A[low]
                low, high = low + 1, high - 1
        return low
    return sort(0, len(A) - 1)   


def printStep(arr, val):
    print("  %2d Step =  " % val, end='')
    print(arr)


my_list = [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]
bubble_sort(my_list.copy())
print("##################################################")
selection_sort(my_list.copy())
print("##################################################")
print("시작 : ", my_list)
quick_sort(my_list)
print("결과 : ", my_list)
