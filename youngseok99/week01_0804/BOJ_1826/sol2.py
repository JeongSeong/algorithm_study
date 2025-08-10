def greedy(L, P, stations):
    priority_queue = [] # 우선순위 큐
    count = 0
    for station, fuel in stations:
        while P < station: # 지금 탐색하는 곳에 도달하지 못할 것 같으면
            if priority_queue: # 충전할 곳이 있었으면
                P -= heapq.heappop(priority_queue) # 가장 큰 충전소를 충전했다 가정하고
                count += 1 # 그 충전한 숫자를 센다
            else: # 여기까지 충전할 곳이 없었으면
                return -1 # -1을 반환한다
        if station >= L: # 만약 여기가 목적지였다면
            break # 더이상 연산을 하지 않고 끝낸다
        heapq.heappush(priority_queue, -fuel) # 도착했으면 현재 충전소의 충전량을 기록한다

    return count # 충전할 곳이 계속 있어야 끝까지 올 수 있으므로 최종 충전 수를 바로 반환한다.


if __name__ == "__main__":
    N = int(input())
    stations = [tuple(map(int, input().split())) for _ in range(N)]
    L, P = list(map(int, input().split()))
    stations.append((L, 0))
    stations.sort()

    print(greedy(L, P, stations))