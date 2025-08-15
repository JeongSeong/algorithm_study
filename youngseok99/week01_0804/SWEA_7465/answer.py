T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    relation = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        first, second = list(map(int, input().split()))
        relation[first].append(second)
        relation[second].append(first)

    result = 0
    stack = []
    not_visited = set(range(1, N+1))
    while not_visited:
        result += 1
        start = not_visited.pop()
        stack.append(start)
        while stack:
            current = stack.pop()
            for i in relation[current]:
                if i in not_visited:
                    stack.append(i)
                    not_visited.remove(i)

    print(f"#{test_case} {result}")