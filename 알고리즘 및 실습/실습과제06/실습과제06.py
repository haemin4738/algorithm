import math
import time
import random

def dist(p1, p2):   # 두 점 사이의 거리를 계산하는 함수
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair_dist(points):   # 최근접 점의 쌍을 찾는 함수    
    n = len(points)
    if n <= 1:  # 점이 하나 이하인 경우 거리를 구할 수 없으므로 none,none과 무한대값을 반환
        return None, None, float('inf')
    elif n == 2:    # 점이 두개인 경우 거리를 계산하여 반환
        return points[0], points[1], dist(points[0], points[1])

    # x좌표에 대해 정렬한 후, 가운데를 기준으로 그룹을 나눔
    mid = n // 2
    left_points = points[:mid]
    right_points = points[mid:]

    # 왼쪽 그룹과 오른쪽 그룹에서 각각 가장 가까운 두 점의 쌍을 재귀 함수로 찾음
    left_p1, left_p2, left_dist = closest_pair_dist(left_points)
    right_p1, right_p2, right_dist = closest_pair_dist(right_points)

    # 두 그룹에서 찾은 가장 가까운 두 점의 쌍 중 거리가 더 작은 쌍을 선택
    if left_dist < right_dist:
        min_p1, min_p2, min_dist = left_p1, left_p2, left_dist
    else:
        min_p1, min_p2, min_dist = right_p1, right_p2, right_dist

    # 가운데를 가로지르는 선을 기준으로 가장 가까운 두 점의 쌍을 찾음
    split_points = []
    for point in points:
        if abs(point[0] - points[mid][0]) < min_dist:
            split_points.append(point)
    split_points.sort(key=lambda x: x[1])   # 점들을 x로 정렬
    for i, p1 in enumerate(split_points):
        for p2 in split_points[i+1:i+8]:
            if dist(p1, p2) < min_dist:
                min_p1, min_p2, min_dist = p1, p2, dist(p1, p2)

    return min_p1, min_p2, min_dist

def closest_pair_dist2(P, n):
    if n <= 3:
        return closest_pair(P)
    mid = n // 2
    mid_x = P[mid][0]

    dl = closest_pair_dist2(P[:mid], mid)
    dr = closest_pair_dist2(P[mid:], n - mid)
    d = min(dl, dr)

    Pm = []
    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])

    ds = strip_closest(Pm, d)
    return min(d, ds)

def strip_closest(P, d):
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[0])

    for i in range(n):
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = dist(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

def closest_pair(p):
    n = len(p)
    mindist = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            dist2 = dist(p[i], p[j])
            if dist2 < mindist:
                mindist = dist2
    return mindist

points = []
for i in range(10000000):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    points.append((x, y))

points2 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

start_time = time.time()
result = closest_pair_dist2(points, len(points))
end_time = time.time()
print("(개선 전) 소요 시간 : ", end_time - start_time)

start_time = time.time()
result = closest_pair_dist(points)
end_time = time.time()
print("(개선 후) 소요 시간 : ", (end_time - start_time))
print("가장 가까운 두 점과 거리", result)