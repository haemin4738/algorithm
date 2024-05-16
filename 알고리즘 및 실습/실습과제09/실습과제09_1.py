# 올라온 문제 2개 or 연습문제 6번
# W: 배낭의 최대 무게
# wt: 각 아이템의 무게를 담은 리스트
# val: 각 아이템의 가치를 담은 리스트
# n: 아이템의 개수
def knapSack_memo(W, wt, val, n, A):
    if A[n][W] != -1: # 만약 A[n][W]이 이미 계산된 경우
        return A[n][W] # A[n][W] 값을 반환합니다.

    if n == 0 or W == 0: # 만약 n=0 이거나 W=0인 경우
        A[n][W] = 0 # # A[n][W] 값은 0입니다.
    
    elif wt[n - 1] > W: # 만약 wt[n-1]이 W보다 큰 경우
        A[n][W] = knapSack_memo(W, wt, val, n - 1, A) # # n-1번째 아이템을 선택할 수 없습니다.
    # n-1번째 아이템을 선택하지 않은 경우와 선택한 경우 중 더 큰 가치를 선택합니다.
    else:
        valWith = val[n - 1] + knapSack_memo(W - wt[n - 1], wt, val, n - 1, A)
        valWithout = knapSack_memo(W, wt, val, n - 1, A)
        A[n][W] = max(valWith, valWithout)

    return A[n][W]

def knapSack_tabulation(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                A[i][w] = A[i - 1][w]
            else:
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)
    return A[n][w]  # 배낭의 최대 가치


val = [60, 100, 190, 120, 200, 150, 90, 70, 30, 170]
wt = [2, 5, 8, 4, 7, 6, 1, 9, 4, 3]
W = 18  # 배낭 용량
n = len(val)  # 물건의 수
print(" 0 - 1 배낭문제(테뷸레이션)", knapSack_tabulation(W, wt, val, n))
