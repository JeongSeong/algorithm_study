from collections import deque

# 보드의 크기
N = int(input())
# 사과의 개수
K = int(input())
apples = {tuple(map(int, input().split())) for _ in range(K)}

# 방향 전환 횟수
L = int(input())
shifts = dict()
for _ in range(L):
    s, d = input().split()
    s = int(s)
    if d == 'D':
        shifts[s] = 1
    else:
        shifts[s] = -1

# sec을 1씩 추가한다
sec = 1

# 방향 전환: 우 하 좌 상 (r, c) D일 경우 (direction+1) % 4
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

# 뱀 초기 설정
snake = deque([(1, 1)])
while True:

    # 다음 이동 좌표를 구함
    nxt_r, nxt_c = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
    # 만약 벽에 부딪히면: 종료
    if nxt_r > N or nxt_c > N or nxt_r < 1 or nxt_c < 1:
        break
    # 만약 자기 몸에 부딪히면: 종료
    elif (nxt_r, nxt_c) in set(snake):
        break

    if (nxt_r, nxt_c) in apples:
        # 사과가 있을 경우 - head만 이동
        apples.discard((nxt_r, nxt_c))
    elif (nxt_r, nxt_c) not in apples:
        # 사과가 없을 경우 - head와 tail 이동
        snake.pop()

    snake.appendleft((nxt_r, nxt_c))

    # 현재 시간이 방향 전환 시간과 동일하다면 - x초가 끝난 뒤에:
    if sec in shifts:
        direction = (direction + shifts[sec]) % 4
    sec += 1
print(sec)