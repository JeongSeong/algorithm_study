# 1h 22m
import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_road(r, c, now, length, visited, flag):
    '''
    :param r: 입력 row
    :param c: 입력 col
    :param now: 현재 값
    :param length: 길의 길이
    :param visited: 방문 여부
    :param flag: 공사 여부
    :return:
    '''
    global max_length
    # Debug: 입력 값들을 출력해봄
    # print(f'(r, c): ({r}, {c}) / length: {length} / flag: {flag}')

    # 현재 길이가 최대 길이보다 길다면 최대 길이 갱신
    if length > max_length:
        max_length = length

    # r, c에서 출발해 더 낮은 곳으로 내려온다 - 다음 값을 확인
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if visited[nr][nc]:
            continue
        # 만약 다음 값이 현재 값보다 작으면: 그냥 내려감
        if grid[nr][nc] < now:
            visited[nr][nc] = 1
            find_road(nr, nc, grid[nr][nc], length+1, visited, flag)
            visited[nr][nc] = 0
        # 만약 다음 값이 현재 크거나 같은데, flag가 0이고 차가 K 이하라면 flag를 사용해봄
        elif not flag and (grid[nr][nc] - now + 1) <= K:
            visited[nr][nc] = 1
            next = now - 1
            find_road(nr, nc, next, length+1, visited,1)
            visited[nr][nc] = 0
        # 만약 다음 값이 현재 값보다 크거나 같은데, flag가 1이면 continue

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리의 높이를 탐색한다 - 모든 행을 합해 하나의 리스트 만들기
    sorted_list = []
    for row in grid:
        sorted_list += row
    sorted_list.sort()

    max_height = sorted_list[-1]    # 가장 높은 봉우리
    max_length = 1  # 가장 긴 등산로 길이
    # 가장 높은 지점 좌표들을 저장한 리스트
    start_points = []
    # 가장 높은 봉우리의 좌표를 저장한다 - 새로운 리스트 생성
    for r in range(N):
        for c in range(N):
            if grid[r][c] == max_height:
                start_points.append((r, c))

    # 가장 높은 봉우리부터 주변을 탐색하며 내려와본다
    for r, c in start_points:
        # 매번 visited를 만들어줌
        visited = [[0] * N for _ in range(N)]
        visited[r][c] = 1
        find_road(r, c, max_height, 1, visited,0)
    print(f'#{tc} {max_length}')
