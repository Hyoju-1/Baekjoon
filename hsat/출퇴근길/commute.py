import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    rev[y].append(x)              # 방향을 뒤집어서 저장
S, T = map(int, input().split())

def bfs(start, g, block):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == block:          # 목적지에 도착하면 더 나아가지 않음
            continue
        for nxt in g[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return visited

a = bfs(S, graph, T)      # ① S에서 갈 수 있음 (T에서 멈춤)
b = bfs(T, rev , 0)          # ② T로 갈 수 있음 (뒤집은 그래프, 멈춤 없음)
c = bfs(T, graph, S)      # ③ T에서 갈 수 있음 (S에서 멈춤)
d = bfs(S, rev, 0)        # ④ S로 갈 수 있음 (뒤집은 그래프, 멈춤 없음)

count = 0
for v in range(1, n + 1):
    if v == S or v == T:
        continue
    if a[v] and b[v] and c[v] and d[v]:                 # 네 조건이 모두 True이면
        count += 1
print(count)