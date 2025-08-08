'''
마을에 n 명의 사람이 살고 있고, 사람에 1 번부터 n 번 까지 번호가 붙여져 있다.
두 사람은 서로를 알고 있는 관계일 수도 있고, 아닐수도 있다.
두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면
이러한 사람들을 다 묶어서 하나의 무리라고 한다.
이 마을에 몇 개의 무리가 존재하는지 계산해라.

다음 코드는 공개된 두개의 테스트 케이스는 통과하였으나, 제출을 해보니 런타임 에러가 났다.
'''

def min_circle(set_list):
    if len(set_list)==1:
        return set_list
    q = set_list[:]

    while True:
        new = [q.pop(0)]
        do_stop = len(q)
        while q:
            c = q.pop(0)
            do_append = True
            for i in range(len(new)):
                if new[i].intersection(c):
                    new[i] = new[i].union(c)
                    do_append = False
                    break
            if do_append:
                new.append(c)
                do_stop -= 1
        q = new[:]
        if (do_stop == 0) or (len(new)==1):
            break
    return q

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    
    acq = []
    for _ in range(m):
        acq.append(set(map(int, input().split())))
        
    circles = min_circle(acq)

    print(f'#{tc} {len(circles)}')