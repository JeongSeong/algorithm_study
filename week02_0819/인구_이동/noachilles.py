from collections import deque

# N: 나라의 개수, L, R: 국경선 여는 기준이 되는 수치
N, L, R = map(int, input().split())

A = [list(map(int, input().split()))[:N] for _ in range(N)]

# 상 하 좌 우
d_r = [-1, 1, 0, 0]
d_c = [0, 0, -1, 1]

def bfs(ir, ic):
    union_list = [(ir, ic)] # 서로 연합이 된 나라의 리스트
    queue = deque([(ir, ic)])   # BFS를 위한 queue
    visited[ir][ic] = 1 # 방문 처리
    popularity_sum = A[ir][ic]  # 인구 합
    union_cnt = 1   # 연합국가 개수
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + d_r[d], c + d_c[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:continue  # 범위 벗어나면 pass
            elif visited[nr][nc]: continue  # 방문했으면 pass
            elif abs(A[r][c] - A[nr][nc]) < L or abs(A[r][c] - A[nr][nc]) > R:
                continue # L, R 범위까지 만족할 경우
            queue.append((nr, nc))
            union_list.append((nr, nc))
            visited[nr][nc] = 1
            popularity_sum += A[nr][nc]
            union_cnt += 1
    if popularity_sum > A[ir][ic]:
        move(union_list, popularity_sum, union_cnt)
        return 1
    return 0

# bfs로부터 받은 연합 목록, 총 인구 수, 연합국에 속한 국가 수로부터 A를 변화시킴
def move(union_list, popularity_sum, union_cnt):
    for r, c in union_list:
        A[r][c] = popularity_sum // union_cnt
    return

res = 0
for day in range(2000 + 1):
    # 서로서로의 칸을 연결 - 첫번째 칸부터 국경선을 연다
    # BFS로 국경선 오픈 여부 확인 - 국경선 열기
    visited = [[0] * N for _ in range(N)]
    # 인구 이동 여부 - 변함이 없으면 break
    moved = False
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 1:
                continue
            else:
                if bfs(r, c):
                    moved = True
    if not moved:
        res = day
        break
print(day)