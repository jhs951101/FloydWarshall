n = 5
roots = [[1,2,3], [1,3,6], [2,4,5], [3,4,8], [3,5,1], [4,5,2]]

# n: 총 노드의 수
# roots: 간선 정보들 - [노드A, 노드B, 비용]

INF = int(1e9)
graph = [ [INF] * (n+1) for _ in range(n+1) ]

# INF: 무한대 값
# graph: 최단 거리를 담는 표 (최단 거리 = graph[출발지][도착지])

# 재귀적 간선(노드A -> 노드A)은 없으므로 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 간선 정보를 표에 삽입
# 양방향으로 이동 가능하므로, '노드A -> 노드B', '노드B -> 노드A', 이렇게 2번 삽입
for arr in roots:
    graph[ arr[0] ][ arr[1] ] = arr[2]
    graph[ arr[1] ][ arr[0] ] = arr[2]

for z in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # z: 경유지
            # a: 출발지
            # b: 도착지
            # 경유점을 거쳐 가는 값이 더 작으면 더 작은 값으로 대체
            graph[a][b] = min(graph[a][b], graph[a][z] + graph[z][b])

# 모든 최단 거리 출력
for x in range(1, n+1):
    for y in range(1, n+1):
        if graph[x][y] == INF:
            print('N', end='  ')
        else:
            print(graph[x][y], end='  ')

    print()
