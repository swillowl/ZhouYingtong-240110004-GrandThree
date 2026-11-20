"""30分钟：只补全dijkstra_path。5分钟初始化、15分钟核心、3分钟边界、7分钟测试修正。"""
import heapq
from support import RunSupport

def dijkstra_path(graph,start,goal,recorder=None):
    # 开始实现时删除下一行；保留函数名、参数和返回格式。
    # raise NotImplementedError('请先完成dijkstra_path')
    run=RunSupport('dijkstra',recorder,start,goal)
    if not graph.passable(start) or not graph.passable(goal):return run.failure(blocked=True)
    # TODO 1：heap=[(0,start[0],start[1],start)]；best={start:0}；came_from={}；closed=set()。
    heap=[(0,start[0],start[1],start)];best={start:0};came_from={};closed=set()
    # TODO 2：while heap：取出(g,_r,_c,current)=heapq.heappop(heap)。
    #   如果current在closed中就continue；否则closed.add(current)。
    #   run.expand(current,len(heap),g)
    #   若current==goal：return run.success(came_from,start,goal,g)
    #   遍历graph.neighbors(current)：已closed的跳过。
    #   candidate=____+graph.cost(____,____)
    #   如果candidate严格小于best.get(nxt,float('inf'))：
    #       同时更新best[nxt]与came_from[nxt]；heappush(heap,(candidate,nxt[0],nxt[1],nxt))。
    #       run.relax(nxt,current,candidate)
    while heap:
        g,_r,_c,current=heapq.heappop(heap)
        if current in closed:continue
        closed.add(current)
        run.expand(current,len(heap),g)
        if current==goal:return run.success(came_from,start,goal,g)
        for nxt in graph.neighbors(current):
            if nxt in closed:continue
            candidate=g+graph.cost(current,nxt)
            if candidate<best.get(nxt,float('inf')):
                best[nxt]=candidate
                came_from[nxt]=current
                heapq.heappush(heap,(candidate,nxt[0],nxt[1],nxt))
                run.relax(nxt,current,candidate)
    # TODO 3：堆耗尽仍无路：return run.failure()
    return run.failure()
