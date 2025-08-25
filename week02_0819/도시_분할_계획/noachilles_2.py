import sys
sys.stdin = open('input.txt')

# kruskal

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y

N, M = map(int,input().split())

# O(M)
edges = [list(map(int, input().split())) for _ in range(M)]

# O(N)
parent = [i for i in range(N+1)]

# O(MlogM)
edges.sort(key=lambda x:x[2])

# 답 weight_sum / 구하기 위한 max_weight
weight_sum, max_weight = 0, 0
# O(M)
for edge in edges:
    x, y, w = edge
    # 만약 두 노드가 같은 부모에 속해있지 않으면:
    # 합친다
    if find_set(x) != find_set(y):
        weight_sum += w
        max_weight = w  # 오름차순 정렬
        union(x, y)

# 답 구하기
weight_sum -= max_weight
print(weight_sum)