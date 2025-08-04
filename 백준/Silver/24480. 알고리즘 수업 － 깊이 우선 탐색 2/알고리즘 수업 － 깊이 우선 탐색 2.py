import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가
input = sys.stdin.readline

# 입력 처리
N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

# 간선 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 내림차순 정렬
for i in range(1, N + 1):
    graph[i].sort(reverse=True)

visited = [False] * (N + 1)
order = [0] * (N + 1)  # 방문 순서 저장
cnt = 1


def dfs(v):
    global cnt
    visited[v] = True
    order[v] = cnt
    cnt += 1

    for next in graph[v]:
        if not visited[next]:
            dfs(next)

# DFS 시작
dfs(R)

# 출력
for i in range(1, N + 1):
    print(order[i])
