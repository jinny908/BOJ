import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t)) # 튜플로 값 고정
    reverse_graph[b].append((a, t))

def dijkstra(start, graph):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start)) # ( 거리, 노드 ) heap 에 추가
    # why 거리, 노드 ? -> heapq 는 튜플을 비교할 때, 첫번째 원소를 기준으로 정렬

    while heap:
        dist, now = heapq.heappop(heap) # heap 에서 가장 짧은 거리 노드 꺼냄
        if distance[now] < dist: # 이미 b 번 노드를 더 짧은 거리로 방문 했으면 스킵
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost  < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    return distance

# X → 각 마을 (돌아가는 길)
back = dijkstra(x, graph)

# 각 마을 → X (가는 길)
go = dijkstra(x, reverse_graph)

max_time = 0
for i in range(1,n + 1):
    total_time = go[i] + back[i]
    max_time = max(total_time, max_time)

print(max_time)