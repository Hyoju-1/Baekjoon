T = int(input())  # 테스트 케이스 개수
dp = [0] * 12  # 문제 조건에서 n < 11
# 초기값 설정
dp[1] = 1  # (1)
dp[2] = 2  # (1+1, 2)
dp[3] = 4  # (1+1+1, 1+2, 2+1, 3)

# 점화식으로 채우기
for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 케이스별 출력
for _ in range(T):
    n = int(input())
    print(dp[n])