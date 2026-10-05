import sys
from collections import deque
input = sys.stdin.readline

# ── 입력 ──
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
people = list(map(int, input().split()))

# ── 그래프 BFS (아까 드린 틀 그대로) ──
def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist

# ── 1. 사람마다 거리표 만들기 (표의 각 행) ──
dists = []
for p in people:
    dists.append(bfs(p))

# ── 2. 노드마다 점수 계산 (표의 각 열) ──
ans = float('inf')
for v in range(1, n + 1):
    ok = True
    worst = 0
    for d in dists:
        if d[v] == -1:          # 이 사람이 v에 못 오면
            ok = False
            break
        worst = max(worst,d[v])  # 가장 오래 걸리는 시간 갱신
    if ok:
        ans = min(ans, worst)      # 노드 점수 중 최솟값

# ── 3. 출력 ──
if ans == float('inf'):
    print(-1)
else:
    print(ans)