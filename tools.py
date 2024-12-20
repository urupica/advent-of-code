############################
# shortest path algorithms #
############################

# a) breadth-first-search (for unweighted graphs, e.g. labyrinths)
from collections import deque

def get_neighbors(v):
    # needs implementation, return all neighbors of v
    return []

def bfs(start, end):
    queue = deque()
    dist = {start: 0}
    queue.append(start)
    # prev = {}
    while queue:
        v = queue.popleft()
        if v == end:
            # path = [v]
            # while v != start:
            #     v = prev[v]
            #     path.append(v)
            # path.reverse()
            # return path
            return dist[v]
        for w in get_neighbors(v):
            if w not in dist:
                dist[w] = dist[v] + 1
                queue.append(w)
                # prev[w] = v


# b) dijkstra's algorithm
from heapq import heappush, heappop

def get_weighted_neighbors(v):
    # needs implementation, return all neighbors of v with their weights
    return []

def dijkstra(start, end):
    dist = {start: 0}
    visited = set()
    heap = []
    heappush(heap, (0, start))
    # prev = {}
    while heap:
        dv, v = heappop(heap)
        if v == end:
            # path = [v]
            # while v != start:
            #     v = prev[v]
            #     path.append(v)
            # path.reverse()
            # return path
            return dv

        if v in visited:
            continue
        visited.add(v)

        for w, dvw in get_weighted_neighbors(v):
            dw = dv + dvw
            if w not in visited and (w not in dist or dw < dist[w]):
                dist[w] = dw
                heappush(heap, (dw, w))
                # prev[w] = v
