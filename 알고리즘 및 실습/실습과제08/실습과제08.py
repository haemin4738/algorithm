NO_OF_CHARS = 128

def string_match(text, pattern):
    comparisons = 0  # 비교 연산 횟수를 저장하는 변수
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            comparisons += 1  # 비교 연산 횟수 증가
            if text[i+j] != pattern[j]:
                match = False
                break
        if match:
            return i, comparisons  # 일치하는 인덱스와 비교 연산 횟수 반환
    return -1, comparisons  # 일치하는 부분이 없는 경우 -1과 비교 연산 횟수 반환

def shift_table(pattern):
    m = len(pattern)
    tb1= [m] * NO_OF_CHARS
    for i in range(m - 1):
        tb1[ord(pattern[i])] = m - 1 - i

    return tb1

def search_horspool(text, pattern):
    m = len(pattern)
    n = len(text)
    t = shift_table(pattern)
    i = m - 1
    compare_count = 0  # 비교 횟수를 저장할 변수 추가
    while i <= n - 1:
        k = 0
        while k <= m - 1 and pattern[m - 1 - k] == text[i - k]:
            k += 1
            compare_count += 1  # 내부 루프에서 비교한 문자열 개수를 더함
        if k == m:
            return i - m + 1, compare_count
        else:
            i += t[ord(text[i])]
            compare_count += 1  # 외부 루프에서 비교한 문자열 개수를 더함
    return -1, compare_count

#text = "I_LOVE_BANANA_YOU_LIKE_APPLE_AND_MANGO"
#pattern = "APPLE"
#text = "The future depends on what we do in the present"
#pattern = "present"
text = "In study, it's not the lack of time, but lack of effort."
pattern = "effort"
index, compare_count = string_match(text, pattern)
hors_index, hors_compare_count = search_horspool(text, pattern)

print("호스풀 알고리즘")
if hors_index != -1:
    print(f"패턴이 일치하는 위치: {hors_index}")
else:
    print("패턴을 찾을 수 없습니다.")

print(f"비교한 문자열 개수: {hors_compare_count}")
print("억지기법")
if index != -1:
    print(f"패턴이 일치하는 위치: {index}")
else:
    print("패턴을 찾을 수 없습니다.")

print(f"비교한 문자열 개수: {compare_count}")
        