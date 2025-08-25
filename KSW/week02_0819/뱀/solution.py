#   오 위 왼 아
dy=[0,-1,0,1]
dx=[1,0,-1,0]
# +1 -> L
# -1 -> D

N=int(input()) #크기 N의 보드
board=[[0 for _ in range(N)] for _ in range(N)]

K=int(input()) #보드 위의 사과
for _ in range(K):
    y,x=map(int,input().split())
    board[y-1][x-1]=1

L=int(input()) 
commands=[]
for _ in range(L):
    X,C=input().split()
    commands.append([int(X),C])

t,c=commands.pop(0)
board[0][0]=2 #뱀이 있는 위치는 2로 표시
time,d=0,0 #시간,방향
snake=[[0,0]] #뱀의 위치
start,end=0,0 #뱀의 머리,꼬리 위치

while True:

    y,x=snake[-1] #뱀의 머리 위치
    #print("here!",y,x,time,d)

    if time==t:
        #1.방향 바꾸기
        if c=='L':
            d=(d+1)%4
        else: d=(4+d)%4-1
        #2.다음 코맨드로
        if commands:
            t,c=commands.pop(0)

    ny,nx=y+dy[d],x+dx[d]

    if (0<=ny<N and 0<=nx<N) and board[ny][nx]!=2:
        #만약 사과가 없다면 몸 길이를 줄여야함
        if board[ny][nx]==0:
            ty,tx=snake[end]
            board[ty][tx]=0
            end+=1
        board[ny][nx]=2 #머리 이동
        snake.append([ny,nx])
        time+=1 #시간 증가

    #자기 몸에 부딪히거나 벽이라면 stop
    else: break

print(time+1)