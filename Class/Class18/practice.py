"""只修改标有TODO的 priority 和 relax；其余搜索骨架已经提供。"""
from provided import search


def priority(g, h):
    """TODO 1：返回候选排队使用的 f。g与h使用相同的体力点单位。
    Dijkstra 会传入 h=0；A星会传入给定的剩余估计。
    """
    # raise NotImplementedError("TODO 1：补出 f 的计算")
    return g + h


def relax(g, parent, u, v, edge_cost):
    """TODO 2：尝试用 u 到 v 的边改进记录。
    g是每个位置当前最少累计花费的字典，parent是来路字典。
    先算“到u的累计 + 这一段花费”。仅在更便宜时修改g[v]和parent[v]。
    修改了返回True；没有修改返回False。相等时也不改。
    """
    # raise NotImplementedError("TODO 2：比较累计值，并同步更新花费和来路")
    candidate = g[u] + edge_cost
    if candidate < g[v]:
        g[v] = candidate
        parent[v] = u
        return True
    return False


def dijkstra(graph, start, goal):
    """完整搜索入口：不使用目标估计。"""
    return search(graph, start, goal, {}, priority, relax)


def astar(graph, start, goal, heuristic):
    """完整搜索入口：优先处理 f=g+h 小的候选。"""
    return search(graph, start, goal, heuristic, priority, relax)
