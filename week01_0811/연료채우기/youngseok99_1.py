def search_DFS(L, P, stations, current_station=0, current_fuel=0, fueled_station=0):
    if current_fuel < stations[current_station][0]:
        return 0
    elif current_fuel >= L:
        return fueled_station
    else:
        not_fueled = search_DFS(L, P, stations, current_station+1, current_fuel, fueled_station)
        fueled = search_DFS(L, P, stations, current_station+1, current_fuel+stations[current_station][1], fueled_station+1)
        if not_fueled:
            return min(not_fueled, fueled)
        else:
            return fueled

if __name__ == "__main__":
    N = int(input())
    stations = [tuple(map(int, input().split())) for _ in range(N)]
    stations.sort()
    L, P = list(map(int, input().split()))
    stations.append((L, 0))


    result = search_DFS(L, P, stations, current_fuel=P)
    if result == 0 and L > P:
        result = -1
    print(result)