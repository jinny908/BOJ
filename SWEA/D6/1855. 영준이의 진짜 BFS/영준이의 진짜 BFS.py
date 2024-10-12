from collections import deque
 
T = int(input())
 
def lca(node1, node2):
    global answer
    while depth[node1] > depth[node2]:
        answer += 1
        node1 = child_parent[node1]
    while depth[node1] < depth[node2]:
        answer += 1
        node2 = child_parent[node2]
    while node1 != node2:
        answer += 2
        node1 = child_parent[node1]
        node2 = child_parent[node2]
    return
 
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
 
    answer = 0
    N = int(input())
    input_list = list(map(int, input().split()))
 
    i = 2

    parent_child = [[] for _ in range(N+1)]
    child_parent = [0] * (N+1)
    depth = [0] * (N+1)
 
    depth[1] = 1
    for parent in input_list:
        parent_child[parent].append(i)
        child_parent[i] = parent
        depth[i] = depth[parent] + 1
        i += 1
 
    queue = deque([1])
    # queue.extend(parent_child[1]) # 일단 루트 노드의 자식 노드들부터 큐에 넣어준다
 
    cur_node = 1
    while queue:
        search_node = queue.popleft()
 
        for child in parent_child[search_node]:
            queue.append(child)
            lca(cur_node, child)
            cur_node = child
 
    print('#{} {}'.format(test_case,answer))