#시간 초과 이슈로 pypy3로 제출

import heapq

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    ra,rb=find(a),find(b)
    if ra>rb:
        parents[ra]=rb
    elif ra<rb:
        parents[rb]=ra

#최소신장트리
N,M=map(int,input().split())

#시간복잡도를 줄이기 위해 힙 자료구조 사용
edges=[]
for _ in range(M):
    a,b,c=map(int,input().split())
    edges.append([c,a,b]) #cost,a-b
heapq.heapify(edges) 

cost=0
parents=[i for i in range(N+1)]
cnt=N
for _ in range(M):
    if cnt==2:
        break

    c,a,b=heapq.heappop(edges)
    if find(a)!=find(b):
        union(a,b)
        cost+=c
        cnt-=1

print(cost)

# MST 말고 PRIM 알고리즘으로도 가능하다고 하던데
# 어떻게 구현해야할까???