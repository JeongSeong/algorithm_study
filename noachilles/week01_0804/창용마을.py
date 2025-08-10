# 32min
import sys
sys.stdin = open('s_input.txt')

def make_group(person):
    visited[person] = 1
    check_list = [person]
    # check_list에서 한 명씩 호출
    while check_list:
        now = check_list.pop(0)
        for nxt in connection[now]:
            # 만약 방문한 적 없다면
            if not visited[nxt]:
                # 확인 리스트에 추가
                visited[nxt] = 1
                check_list.append(nxt)
    return 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    connection = [[] for _ in range(N+1)]
    # 이후 M개 줄에 걸쳐 서로를 알고 있는 두 사람 번호
    # 서로의 connection에 저장
    for _ in range(M):
        a, b = map(int, input().split())
        connection[a].append(b)
        connection[b].append(a)

    # 마을 사람을 돌면서 무리를 알아내자
    # 무리의 개수 group_num
    group_num = 0

    # 주민 조회 여부
    visited = [0] * (N+1)
    for i in range(1, N+1):
        # 조사한 적이 없을 때만 탐색한다
        if not visited[i]:
            group_num += make_group(i)

    print(f'#{tc} {group_num}')