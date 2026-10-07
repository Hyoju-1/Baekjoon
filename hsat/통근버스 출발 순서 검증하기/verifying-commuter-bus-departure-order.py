from itertools import combinations

N = int(input())
sequence = list(map(int, input().split()))



# Please write your code here.

cnt = 0

for i in range(N):
    small = 0
    for j in range(N-1,i,-1):
#   j를 오른쪽 끝에서 i 바로 다음까지 왼쪽으로 이동하며
        if sequence[j] > sequence[i] :
            cnt += small
#     a[j]가 a[i]보다 크면: 답에 small을 더한다
        if sequence[j] < sequence[i] :
            small +=1
#     a[j]가 a[i]보다 작으면: small을 1 늘린다
print(cnt)