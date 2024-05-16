def lost_check(A):
    n = len(A)      # 리스트의 길이
    total_sum = (n + 1) * (n + 2) // 2 # 1부터 n까지 수열의 합 
            # 길이가 n 이므로 수열의 마지막 수는 n + 1 이다.
    cur_sum = sum(A)    # 리스트의 합

    if total_sum - cur_sum == 0:
        return True
    else:
        return total_sum - cur_sum
    
my_data = [1, 2, 3, 4, 5, 6, 8, 9]
if(lost_check == True): print("빠진 수는 없습니다.")
else: print("빠진 수는 : ", lost_check(my_data))