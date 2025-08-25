from collections import deque
import sys
input=sys.stdin.readline

#3.함수정의
dx=[-1,0,0,1]
dy=[0,1,-1,0]

def bfs(y,x):
    queue=deque([[y,x]])
    country=[[y,x]]
    sum_people=people[y][x]
    visited[y][x]=True

    while queue:
        ty,tx=queue.popleft()

        for d in range(4):
            ny=ty+dy[d]
            nx=tx+dx[d]

            #범위를 벗어나지 않으면
            #방문하지 않았고
            #차이가 L이상 R이하라면
            if 0<=ny<N and 0<=nx<N:
                if not visited[ny][nx]:
                    if L<=abs(people[ty][tx]-people[ny][nx])<=R:
                        queue.append([ny,nx])
                        visited[ny][nx]=True
                        country.append([ny,nx])
                        sum_people+=people[ny][nx]

    if len(country)>1:
        for c in country:
            people[c[0]][c[1]]=sum_people//len(country)
        return True
    else: 
        return False


#1.입력받기
# NxN 나라수, L<=차이<=R 라면 open
N,L,R=map(int,input().split())
people=[]
people=deque(people)
for _ in range(N):
    people.append(list(map(int,input().split())))

#2.자료형준비/필요한 변수들

#4.출력
day=0
while True:
    visited=[[False for _ in range(N)] for _ in range(N)]
    move=False
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                if bfs(y,x):
                    move=True
    if not move:
        break

    day+=1

print(day)