# n: 총 노드의 수
# roots: 간선 정보들 - [노드A, 노드B, 간선 비용]
n = 6
roots = [[1,5,3], [1,6,4], [1,3,7], [2,3,3], [2,4,2], [3,5,1], [4,5,6], [4,6,8], [5,6,5]]

INF = int(1e9)
graph = [ [INF] * (n+1) for _ in range(n+1) ]

# 재귀적 간선(노드A -> 노드A)은 없으므로 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 간선 정보를 그래프에 삽입
# 양방향으로 이동 가능하므로 '노드A -> 노드B' & '노드B -> 노드A' 로 2번 삽입
for info in roots:
    graph[ info[0] ][ info[1] ] = info[2]
    graph[ info[1] ][ info[0] ] = info[2]

# z: 경유점, 경유 노드
# a: 출발점
# b: 도착점
for z in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 경유점을 거쳐 가는 값이 더 작으면 더 작은 값으로 대체
            graph[a][b] = min(graph[a][b], graph[a][z] + graph[z][b])

# 각 출발점부터 각 도착점까지 모든 최단 거리 출력
for x in range(1, n+1):
    for y in range(1, n+1):
        if graph[x][y] == INF:
            print('N', end='  ')
        else:
            print(graph[x][y], end='  ')

    print()
