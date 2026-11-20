"""30分钟：只补全bfs_path。5分钟初始化、15分钟循环、3分钟边界、7分钟测试修正。"""
from collections import deque
from support import RunSupport

def bfs_path(graph,start,goal,recorder=None):
    # 开始实现时删除下一行；保留函数名、参数和返回格式。
    # raise NotImplementedError('请先完成bfs_path')
    run=RunSupport('bfs',recorder,start,goal)
    if not graph.passable(start) or not graph.passable(goal):return run.failure(blocked=True)
    # TODO 1：frontier=deque([____])；seen={____}；came_from={}。
    frontier=deque([start])
    seen={start}
    came_from={}    
    # TODO 2：while frontier：
    #   current=frontier.____()    # 为什么从队首取？
    #   run.expand(current,len(frontier))
    #   如果current==goal：return run.success(came_from,start,goal)
    #   逐个看graph.neighbors(current)：已在seen里就continue。
    #   对新邻居：seen.add(____)；came_from[____]=____；frontier.append(____)
    #   run.enqueue(nxt,current,len(frontier))
    while frontier:
        current=frontier.popleft()    # 为什么从队首取？
        run.expand(current,len(frontier))
        if current==goal:return run.success(came_from,start,goal)
        for nxt in graph.neighbors(current):
            if nxt in seen:continue
            seen.add(nxt)
            came_from[nxt]=current
            frontier.append(nxt)
            run.enqueue(nxt,current,len(frontier))

    # TODO 3：队列耗尽仍无路：return run.failure()
    return run.failure()
