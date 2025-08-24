direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
right = {0:3, 3:1, 1:2, 2:0}
left = {0:2, 2:1, 1:3, 3:0}

n = int(input()) # 보드 크기
k = int(input()) # 사과 갯수

# 1 행 1 열이 시작점이고, 벽에 부딧히면 게임 끝남
array = [[0]*(n+2)]
for _ in range(n):
    row = [0] + [1]*n + [0]
    array.append(row)
array.append([0]*(n+2))

for _ in range(k):
    r, c = map(int, input().split())
    array[r][c] = 2 # 사과
L = int(input()) # 방향 변환 횟수
rotate = []
for _ in range(L):
    x, c = input().split()
    # rotate[int(x)] = c # 'L'은 왼쪽 90도 회전, 'D' 는 오른쪽 90도 회전
    rotate.append((int(x), c))

# 몇 초에 게임이 끝나는지 출력. 벽이나 자기자신의 몸과 부딧히면 끝
seconds = 0
ci, cj = 1, 1 
direct = 3 # 맨 처음에 오른쪽을 향함
snake = [(ci, cj)]
array[ci][cj] = 3
while True:
    # 머리는 매번 다음칸
    # 사과 먹으면 꼬리두고 머리 늘림
    # 사과 없으면 꼬리 칸에서 꼬리 뺌
    seconds += 1

    d = direction[direct]
    ni, nj = ci+d[0], cj+d[1] # 머리칸

    if array[ni][nj] == 0: # 벽만남
        break
    elif array[ni][nj] == 3: # 자기 자신의 몸과 부딧힘
        break
    elif array[ni][nj] == 2: # 사과 만남
        # 꼬리두고 머리 늘림. 꼬리를 3으로 함
        ci, cj = ni, nj 
        snake.append((ci, cj))
        array[ci][cj] = 3

    else: # 그냥 감. 꼬리칸에서 꼬리뺌
        ci, cj = ni, nj 
        snake.append((ci, cj))
        array[ci][cj] = 3
        tail = snake.pop(0)
        array[tail[0]][tail[1]] = 1

    if rotate and (rotate[0][0] == seconds):
        r = rotate.pop(0)[1]
        if r == 'L':
            direct = left[direct]
        elif r == 'D':
            direct = right[direct]

print(seconds)
