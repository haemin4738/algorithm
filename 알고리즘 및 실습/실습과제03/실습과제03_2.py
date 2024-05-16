def count_substr(s, start_char, end_char):
    count = 0
    n = len(s)
    for i in range(n - 1): # 처음부터 끝까지
        if s[i] == start_char: # i위치의 문자가 A라면
            for j in range(i + 1, n):   # A가 나온 다음부터 끝까지
                if s[j] == end_char: # j에 나온 문자가 B라면
                    count += 1  # count에 1을 더한다
    return count

def count_substr2(s, start_char, end_char):
    count = 0  # 부분 문자열의 개수를 저장할 변수
    start_count = 0  # 현재까지 발견한 A로 시작하는 부분 문자열의 개수를 저장할 변수
    
    for i in range(len(s)):  # 문자열을 처음부터 끝까지 순회
        if s[i] == start_char:  # 만약 A로 시작하는 문자열을 발견하면
            start_count += 1  # A로 시작하는 부분 문자열의 개수를 증가
        elif s[i] == end_char:  # 만약 B로 끝나는 문자열을 발견하면
            count += start_count  # 현재까지 발견한 A로 시작하는 부분 문자열의 개수를 A로 시작하고 B로 끝나는 부분 문자열의 개수에 누적시킴
            
    return count  # 부분 문자열의 개수를 반환

my_str = "ADBAAEDBA"
print("A로 시작하고 B로 끝나는 부분 문자열의 개수 : ", count_substr(my_str, "A", "B"))  #시간 복잡도 O(n^2)
print("A로 시작하고 B로 끝나는 부분 문자열의 개수 : ", count_substr2(my_str, "A", "B"))  #시간 복잡도 O(n)