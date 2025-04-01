import sys
import heapq

input = sys.stdin.readline

def dijkstra(limit):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap, (0, 1))  # (비용 초과 개수, 현재 노드)

    while heap:
        over_count, now = heapq.heappop(heap)

        if dist[now] < over_count:
            continue

        for to, cost in graph[now]:
            next_over = over_count + (1 if cost > limit else 0)
            if next_over < dist[to]:
                dist[to] = next_over
                heapq.heappush(heap, (next_over, to))

    return dist[N] <= K

# 입력
N, P, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_cost = 0

for _ in range(P):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
    max_cost = max(max_cost, c)

# 이분 탐색
left = 0
right = max_cost
answer = -1

while left <= right:
    mid = (left + right) // 2
    if dijkstra(mid):  # mid보다 큰 간선이 K개 이하라면 → 가능한 경로
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
