from practice import dijkstra

graph = {"S": [("A",5),("T",10)], 
         "A": [("T",3)], 
         "T": []}
result = dijkstra(graph, "S", "T")
print(result.path, result.cost)
# 加一行 assert，核对你先算出的花费。
assert result.cost == 8, f"Expected cost 8, got {result.cost}"