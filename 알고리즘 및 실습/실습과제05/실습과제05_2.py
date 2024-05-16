def findMedianSortedArrays(num1, num2):
    # 리스트 합치기
    for i in num2:
        num1.append(i)
        
        arr = sorted(num1)
        medianIndex = (len(arr) - 1) // 2
        if len(arr) % 2 == 1:
            answer = arr[medianIndex]
        else:
            answer = (float)(arr[medianIndex] + arr[medianIndex + 1]) / 2

    print("병합된 배열 : ", arr)
    print("중앙 값 : ", answer)

num1 = []
num2 = []
print("num1 리스트 입력")
num1 = list(map(int, input().split()))
print("num2 리스트 입력")
num2 = list(map(int, input().split()))
findMedianSortedArrays(num1, num2)
