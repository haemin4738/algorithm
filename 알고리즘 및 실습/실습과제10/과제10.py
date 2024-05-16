def floyd(graph):
    n = len(graph)
    
    # 최단 경로 거리와 최단 경로 행렬 초기화
    dist = [[float('inf')] * n for _ in range(n)]
    path = [[None] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
                path[i][j] = i
    
    # 최단 경로 거리 갱신
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
    
    # 최단 경로 추적
    def reconstruct_path(start, end):
        if path[start][end] is None:
            return []
        
        path_list = [start]
        while start != end:
            start = path[start][end]
            path_list.append(start)
        
        return path_list
    
    return dist, reconstruct_path


# 그래프 예시
graph = [
    [0, 50, 45, 20, 35, float('inf')],
    [25, 0, 10, 15 , 20 ,float('inf')],
    [float('inf'), float('inf'), 0, float('inf'), 30 ,float('inf')],
    [10, 60, 51, 0, 15, float('inf')],
    [float('inf'), float('inf'), 36, float('inf'), 0, float('inf')],
    [float('inf'), float('inf'), 39, float('inf'), 3, 0]
]

distances, shortest_paths = floyd(graph)

# 최단 경로 거리 출력
print("Shortest path distances:")
for row in distances:
    print(row)

# 최단 경로 출력
print("\nShortest paths:")
for i in range(len(graph)):
    for j in range(len(graph)):
        if i != j:
            path = shortest_paths(i, j)
            print(f"Path from {i} to {j}: {path}")
