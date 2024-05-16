def radix_sort(arr):
    # 가장 긴 문자열의 길이를 구함
    max_length = max(len(word) for word in arr)
    # 알파벳 순서에 따라 버킷을 담는 리스트를 초기화
    buckets = [[] for _ in range(26)]
    # 가장 뒤쪽부터 각 자리수에 해당하는 값을 계산
    for i in range(max_length - 1, -1, -1):
        for word in arr:
            # 문자열의 길이가 현재 자리수보다 길 경우,
            # 해당하는 버킷에 문자열을 추가
            if len(word) >= i + 1:
                index = ord(word[i]) - ord('a')
                buckets[index].append(word)
            # 문자열의 길이가 현재 자리수보다 짧을 경우,
            # 항상 a에 해당하는 버킷에 문자열을 추가
            else:
                buckets[0].append(word)
        # 버킷에 저장된 문자열을 꺼내어 다시 arr에 저장
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
            bucket.clear()
    return arr


arr = ["banana", "apple", "orange", "kiwi", "grape", "peach"]
sorted_arr = radix_sort(arr)
print(sorted_arr)