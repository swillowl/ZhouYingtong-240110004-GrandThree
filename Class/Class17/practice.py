"""只补两种探索策略。图、状态记录和路径还原已经给出。"""
from collections import deque
from provided import emit, reconstruct_path, validate_graph


def dfs_path(graph, start, goal, trace=None):
    """用显式栈保留每层未完成的邻居，等价于按顺序递归。"""
    # TODO 1：开始编写时先删除这一行。
    # raise NotImplementedError("TODO 1：完成按邻居顺序走深")
    validate_graph(graph, start, goal)
    parent = {start: None}
    emit(trace, "discover", start, None)
    if start == goal:
        return [start]
    stack = [(start, iter(graph[start]))]
    emit(trace, "expand", start)
    while stack:
        current, neighbors = stack[-1]
        try:
            neighbor = next(neighbors)
        except StopIteration:
            stack.pop()
            emit(trace, "backtrack", current)
            continue
        # TODO 1A：跳过已经发现的点，给新点登记来路。
        if neighbor in parent:
            continue
        parent[neighbor] = current
        emit(trace, "discover", neighbor, current)
        if neighbor == goal:
            # TODO 1C：沿已登记的来路还原路径。
            return reconstruct_path(parent, goal)
        # TODO 1B：加入新位置及它还没检查的邻居。
        # raise NotImplementedError("TODO 1B：继续走深")
        stack.append((neighbor, iter(graph[neighbor])))
        emit(trace, "expand", neighbor)
    return []


def bfs_path(graph, start, goal, trace=None):
    """发现时写parent和入队；首次发现目标立即返回。"""
    # TODO 2：开始编写时先删除这一行。
    # raise NotImplementedError("TODO 2：完成按层探索")
    validate_graph(graph, start, goal)
    parent = {start: None}
    queue = deque([start])
    emit(trace, "discover", start, None)
    emit(trace, "queue", tuple(queue))
    if start == goal:
        return [start]
    while queue:
        # TODO 2A：取出最早进入队列的位置。
        current = queue.popleft()
        emit(trace, "expand", current)
        for neighbor in graph[current]:
            # TODO 2B：跳过已发现的点，给新点登记来路，再加入队尾。
            if neighbor in parent:
                continue
            parent[neighbor] = current
            queue.append(neighbor)
            emit(trace, "discover", neighbor, current)
            emit(trace, "queue", tuple(queue))
            if neighbor == goal:
                return reconstruct_path(parent, goal)
    return []
