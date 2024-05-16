class Graph:
    def __init__(self, edges=None, n=0):
 
        # 그래프의 총 노드 수
        self.n = n
 
        # 인접 목록을 나타내는 목록 목록
        self.adjList = [[] for _ in range(n)]
 
        # 무방향 그래프에 간선 추가
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# 끝점 v에서 시작하는 그래프에서 DFS 수행
def DFS(graph, v, discovered, color):
 
    # 모든 끝점 u, v에 대해 실행
    for u in graph.adjList[v]:
 
        # 끝점 u가 처음으로 탐색되는 경우
        if not discovered[u]:
 
            # 끝점 u가 현재 노드를 발견된 것으로 표시합니다.
            discovered[u] = True
 
            # 현재 노드는 상위 노드와 반대 색상을 가집니다.
            color[u] = not color[v]
 
            # v에 뿌리를 둔 하위 트리의 DFS가 false를 반환하는 경우
            if not DFS(graph, u, discovered, color):
                return False
 
        # 끝점이 이미 발견되었고 색상이
        # 끝점 u와 v가 같으면 그래프가 이분 그래프가 아닙니다.
        elif color[v] == color[u]:
            return False
 
    return True
 
 
# DFS를 사용하여 그래프가 이분 그래프인지 확인하는 함수
def isBipartite(graph):
 
    # 끝점이 발견되었는지 여부를 추적하는
    discovered = [False] * graph.n
 
    #는 DFS의 각 끝점에 할당된 색상(0 또는 1)을 추적합니다.
    color = [False] * graph.n
 
    #는 그래프가 연결되고 방향이 없을 때 모든 노드에서 시작.
    src = 0
 
    #는 소스 끝점을 발견된 것으로 표시하고 색상을 0(False)으로 설정합니다.
    discovered[src] = True
    color[src] = False
 
    # 호출 DFS 절차
    return DFS(graph, src, discovered, color)
 
 
if __name__ == '__main__':
 
    # 그래프 정점 목록
    edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8), (1, 3)]
            # (1, 3) edge를 제거하면 그래프가 bipartite가 됩니다.
 
    # 그래프의 총 노드 수(8, 9)
    # (1,3) 추가 시 9, 제거 시 8
    n = 9
 
    # 주어진 정점에서 그래프 작성
    graph = Graph(edges, n)
 
    if isBipartite(graph):
        print('이분 그래프 입니다.')
    else:
        print('이분 그래프가 아닙니다.')