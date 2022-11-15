package pkg;

public class FloydWarshall {
	
	public int INF = 1000000000;
    // INF: 무한대 값

    public void main() {
        // n: 총 노드의 수
        // roots: 간선 정보들 - {노드A, 노드B, 간선 비용}
        int n = 5;
        int[][] roots = {{1,2,3}, {1,3,6}, {2,4,5}, {3,4,8}, {3,5,1}, {4,5,2}};

        int[][] graph = new int[n+1][n+1];
        // graph: 최단 거리를 담는 표 (최단 거리 = graph[출발지][도착지])

        for(int x=0; x<n+1; x++){
            for(int y=0; y<n+1; y++){
            	graph[x][y] = INF;
            }
        }

        // 재귀적 간선(노드A -> 노드A)은 없으므로 0으로 초기화
        for(int i=1; i<n+1; i++)
            graph[i][i] = 0;

        // 간선 정보를 그래프에 삽입
        // 양방향으로 이동 가능하므로 '노드A -> 노드B' & '노드B -> 노드A' 로 2번 삽입
        for(int i=0; i<roots.length; i++){
            graph[ roots[i][0] ][ roots[i][1] ] = roots[i][2];
            graph[ roots[i][1] ][ roots[i][0] ] = roots[i][2];
        }
        
        for(int z=1; z<n+1; z++){
            for(int a=1; a<n+1; a++){
                for(int b=1; b<n+1; b++){
                    // z: 경유지
                    // a: 출발지
                    // b: 도착지
                    // 경유점을 거쳐 가는 값이 더 작으면 더 작은 값으로 대체
                    graph[a][b] = Math.min(graph[a][b], graph[a][z] + graph[z][b]);
                }
            }
        }

        // 모든 최단 거리 출력
        for(int x=1; x<n+1; x++){
            for(int y=1; y<n+1; y++){
                if(graph[x][y] == INF)
                    System.out.print("N" + "  ");
                else
                	System.out.print(graph[x][y] + "  ");
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {
        FloydWarshall main = new FloydWarshall();
        main.main();
    }
}