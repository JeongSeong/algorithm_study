def DP(L, P, stations):
    before = ([0] * (P+1)) + ([10000000] * (L - P))
    after = before[:]
    for station, fuel in stations:
        for i in range(station, L-fuel+1):
            after[i+fuel] = min(before[i+fuel], before[i]+1)
        before = after
        after = before[:]
    return after[-1]


if __name__ == "__main__":
    N = int(input())
    stations = [tuple(map(int, input().split())) for _ in range(N)]
    L, P = list(map(int, input().split()))
    stations.append((L, 0))
    stations.sort()

    result = DP(L, P, stations)
    if result == 10000000:
        result = -1
    print(result)