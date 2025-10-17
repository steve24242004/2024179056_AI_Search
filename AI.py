from collections import deque
import heapq

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    expanded = 0
    while queue:
        node, path = queue.popleft()
        expanded += 1
        if node == goal:
            return path, expanded
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None, expanded

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    expanded = 0
    while stack:
        node, path = stack.pop()
        expanded += 1
        if node == goal:
            return path, expanded
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None, expanded

def dls(graph, start, goal, limit):
    def recursive_dls(node, path, depth):
        nonlocal expanded
        expanded += 1
        if node == goal:
            return path
        if depth == 0:
            return None
        for neighbor in graph[node]:
            if neighbor not in path:
                result = recursive_dls(neighbor, path + [neighbor], depth - 1)
                if result:
                    return result
        return None

    expanded = 0
    return recursive_dls(start, [start], limit), expanded

def ids(graph, start, goal):
    limit = 0
    total_expanded = 0
    while True:
        path, expanded = dls(graph, start, goal, limit)
        total_expanded += expanded
        if path:
            return path, total_expanded
        limit += 1

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = {}
    expanded = 0
    while pq:
        cost, node, path = heapq.heappop(pq)
        expanded += 1
        if node == goal:
            return path, cost, expanded
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            for neighbor, edge_cost in graph[node].items():
                heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf'), expanded

def greedy_best_first(graph, start, goal, h):
    pq = [(h[start], start, [start])]
    visited = set()
    expanded = 0
    while pq:
        _, node, path = heapq.heappop(pq)
        expanded += 1
        if node == goal:
            return path, expanded
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor]))
    return None, expanded

def a_star(graph, start, goal, h):
    pq = [(h[start], 0, start, [start])]
    visited = {}
    expanded = 0
    while pq:
        f, g, node, path = heapq.heappop(pq)
        expanded += 1
        if node == goal:
            return path, g, expanded
        if node not in visited or g < visited[node]:
            visited[node] = g
            for neighbor, cost in graph[node].items():
                new_g = g + cost
                heapq.heappush(pq, (new_g + h[neighbor], new_g, neighbor, path + [neighbor]))
    return None, float('inf'), expanded
