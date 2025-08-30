#n = 1 → SK이 돌 1개 가져감 → SK 승리
#n = 2 → SK이 1개만 가져갈 수 있음 → 돌 1개 남음 → CY이 가져감 → CY 승리
#n = 3 → SK이 3개 가져가면 끝 → SK 승리
#n = 4 → SK이 1개 가져가면 CY이 3개 가져가고 끝,SK이 3개 가져가면 CY이 1개 가져가고 끝 → 결국 CY 승리
#n = 5 → SK이 1개 가져가면 CY은 4개 상황(=CY 패 상태) → SK 승리
#패턴을 보면 짝수일 때 CY 승, 홀수일 때 SK 승 

n = int(input())

if n % 2 == 0:
    print("CY")
else:
    print("SK")

### DP로 풀기 
n = int(input())

dp = [False] * (n+1)
dp[0] = False
if n >= 1:
    dp[1] = True
if n >= 2:
    dp[2] = False
if n >= 3:
    dp[3] = True

for i in range(4, n+1):
    # 1개 가져가거나 3개 가져가서 상대가 질 수밖에 없으면 이김
    dp[i] = (not dp[i-1]) or (not dp[i-3])

# 결과 출력
if dp[n]:
    print("SK")
else:
    print("CY")
