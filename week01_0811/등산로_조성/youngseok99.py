T = int(input())

# 상하좌우 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, length, board, cut_used):
    global answer, N, K
    # 현재까지의 최대 경로 길이 갱신
    answer = max(answer, length)

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < N and 0 <= ny < N:
            # 1) 그냥 내려가는 경우
            if board[nx][ny] < board[x][y]:
                dfs(nx, ny, length + 1, board, cut_used)

            # 2) 깎아서 내려가는 경우
            elif not cut_used and board[nx][ny] - K < board[x][y]:
                original = board[nx][ny]            # 원래 높이 저장
                board[nx][ny] = board[x][y] - 1     # 현재보다 1 낮게 깎기
                dfs(nx, ny, length + 1, board, True)
                board[nx][ny] = original            # 원상복구


for test_case in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 최고봉 찾기
    max_height = max(max(row) for row in board)
    peak_positions = [(i, j) for i in range(N) for j in range(N) if board[i][j] == max_height]

    answer = 0

    if len(peak_positions) >= 2:
        # 최고점이 여러 개 → 그냥 DFS 시작 (깎기 False 상태)
        for x, y in peak_positions:
            dfs(x, y, 1, board, False)

    else:
        # 최고점이 1개인 경우
        x, y = peak_positions[0]

        # 1) 깎기 없이 DFS
        dfs(x, y, 1, board, False)

        # 2) 최고점을 1~K만큼 깎고 새 DFS
        for cut_depth in range(1, K+1):
            new_board = [row[:] for row in board]
            nx, ny = x, y
            new_board[nx][ny] -= cut_depth

            new_max = max(max(row) for row in new_board)
            new_peaks = [(i, j) for i in range(N) for j in range(N) if new_board[i][j] == new_max]

            for px, py in new_peaks:
                dfs(px, py, 1, new_board, True)

    print(f"#{test_case} {answer}")
