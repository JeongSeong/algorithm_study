# 이건 이렇게 안 풀리겠다!

import sys
sys.stdin = open('input_2.txt')

# 주유소 개수
N = int(input())
# (a: 출발점에서 주유소까지 거리 / b: 그 주유소에서 채울 수 있는 연료량)
stations = []
oil_list = []
for _ in range(N):
    a, b = map(int, input().split())
    stations.append(a)
    oil_list.append(b)

# L: 출발점에서 마을까지의 거리 / P: 출발할 때 탱크에 있는 연료량
L, P = map(int, input().split())

now = 0 # 현재 위치
oil = P # 현재 연료량
# 가장 가까운(뒤에 있는) 주유소, 그곳에서 충전할 수 있는 연료량, 당시 남은 연료량
s_index = -1
nearest, available, backthen = [-1] * 3
visited = set()
flag = 0
while True:
    print(f'now: {now}, oil: {oil}, nearest: {nearest}')
    # 만약 L에 도착했다면 - 종료
    if now >= L and oil >= 0:
        break
    # 만약 기름이 다 떨어져서 여기까지 올 수 없다면 - 가장 가까운 곳으로
    if oil < 0:
        if nearest < 0 or nearest in visited:
            flag = 1
            break
        now, oil = nearest, available + backthen
        visited.add(nearest)
    # 만약 now에 주유소가 있다면 - 일단 저장만 해둔다
    if now in set(stations):
        s_index += 1
        nearest, available = stations[s_index], oil_list[s_index]
        backthen = oil
    # 한 칸 앞으로 가면서, 연료를 사용
    now += 1
    oil -= 1


