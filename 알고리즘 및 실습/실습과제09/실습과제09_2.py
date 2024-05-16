def lcs_memoization(X, Y, m, n):
    if m == 0 or n == 0: # 빈 문자열인 경우
        return 0
    elif X[m - 1] == Y[n - 1]: # 현재 문자가 같은 경우
        return 1 + lcs_memoization(X, Y, m -1 , n - 1) # 현재 값을 저장하고, 이전 값에서 1을 더한 값을 반환
    else:   
        return max(lcs_memoization(X, Y, m, n - 1), lcs_memoization(X, Y, m - 1, n)) # 이전 값 중 큰 값을 저장하고, 해당 값을 반환

def lcs_tabulation(X, Y, m, n):
    # A 배열 생성 및 초기화
    A = [[0] * (n + 1) for i in range(m + 1)]

    # LCS 길이 계산
    for i in range(m + 1):
        for j in range(n + 1):
            # i=0 또는 j=0인 경우, A[i][j] 값은 0
            if i == 0 or j == 0:
                A[i][j] = 0
            elif X[i - 1] == Y[j - 1]: # X[i-1]과 Y[j-1]이 같은 경우
                A[i][j] = 1 + A[i - 1][j - 1] # A[i][j]에 이전 LCS의 길이에서 1을 더한 값을 저장
            else: # X[i-1]과 Y[j-1]이 같지 않은 경우 
                A[i][j] = max(A[i][j - 1], A[i - 1][j]) # A[i][j]에 이전 LCS의 길이를 저장

    return A[m][n]

X = "DATA STRUCTURE"
Y = "PYTHON ALGORITHM"
m = len(X)
n = len(Y)
print("X =", X)
print("Y = ", Y)
print("LCS(메모이제이션) : ", lcs_memoization(X, Y, m ,n))
print("LCS(테뷸레이션) : ", lcs_tabulation(X, Y, m, n))