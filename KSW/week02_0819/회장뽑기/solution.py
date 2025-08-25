#bfs
def bfs(n):
    visited=[False for _ in range(N+1)]
    visited[n]=True
    queue=[[n,0]]
    res=0

    while queue:
        node,score=queue.pop(0)
        res=max(res,score)
        
        for i in range(1,N+1):
            if graph[node][i]==1: #연결이 되어있다면
                if not visited[i]: #방문하지 않았었다면
                    queue.append([i,score+1])
                    visited[i]=True
    
    #회원점수
    return res

#1.입력받기
N=int(input()) #회원 수
graph=[[0 for _ in range(N+1)] for _ in range(N+1)]
while True:
    u,v=map(int,input().split())

    if u==-1 and v==-1:
        break

    graph[u][v]=1
    graph[v][u]=1

ans=[] #정답

#2.자료형 정의

#3.함수
for n in range(1,N+1):
    ans.append(bfs(n))

#4.출력
print(min(ans),ans.count(min(ans)))
for i in range(N):
    if ans[i]==min(ans):
        print(i+1,end=' ')