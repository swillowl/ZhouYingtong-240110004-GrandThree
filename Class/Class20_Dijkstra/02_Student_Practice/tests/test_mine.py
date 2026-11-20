import pytest
from provided import GridGraph
from practice import dijkstra_path
def test_my_variant():
    # pytest.skip('先写预测与assert，再删除这一行')
    g=GridGraph(3,3,blocked={(1,1)},weights={(0,1):2,(1,0):3})
    result=dijkstra_path(g,(0,0),(2,2))
    assert result.found
    assert result.path==((0,0),(0,1),(0,2),(1,2),(2,2))
    assert result.cost==7
    print("测试通过")
