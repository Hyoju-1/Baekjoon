##### 인출 시간이 짧은 사람부터 먼저 세우는 오름차순 정렬임 
### 누적합 계산하고 결과 출력

import sys

input = sys.stdin.readline

# 1) 사람 수 N
n = int(input().strip())

# 2) 각 사람의 인출 시간 리스트
times = list(map(int, input().split()))

# 3) 인출 시간이 짧은 사람부터 줄 세우기 (오름차순 정렬)
times.sort()

# 4) 누적합 계산
total_wait = 0     # 전체 대기 시간 합
cumulative = 0     # 현재까지 누적 시간

for t in times:
    cumulative += t        # 현재 사람까지의 누적 시간
    total_wait += cumulative  # 이 사람의 대기시간을 총합에 추가


print(total_wait)
