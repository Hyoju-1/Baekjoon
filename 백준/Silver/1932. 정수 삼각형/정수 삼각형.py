n = int(input().strip())
triangle = [list(map(int, input().split())) for _ in range(n)]

# dp 테이블 초기화
dp = [[0] * (i+1) for i in range(n)]
dp[0][0] = triangle[0][0]

# DP 진행
for i in range(1, n):          # 1번째 줄부터 n-1번째 줄까지
    for j in range(i+1):       # i번째 줄의 원소 개수는 i+1개
        if j == 0:  # 맨 왼쪽
            # 맨 왼쪽에 있는 원소는 위에서 바로 내려오는 한 가지 길밖에 없음
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:  # 맨 오른쪽
            # 맨 오른쪽에 있는 원소는 위에서 대각선 왼쪽으로 오는 한 가지 길 밖에 없음
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:  # 중간
            # 중간에 있는 원소는 두가지를 선택할 수 있음.
            # 위쪽 대각선 왼쪽 dp[i-1][j-1]에서 내려오거나
            # 위쪽 바로 위 dp[i-1][j]에서 내려오기
            # 두 경로 중 더 큰 값을 선택해서 현재 원소와 더해줌
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

# 마지막 줄에서 최대값 출력
print(max(dp[n-1]))
