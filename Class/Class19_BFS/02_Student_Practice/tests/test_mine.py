import sys
from pathlib import Path
PRACTICE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRACTICE_DIR))
import pytest
from provided import GridGraph
from practice import bfs_path
def test_my_variant():
    # pytest.skip('先写预测与assert，再删除这一行')
    result = bfs_path(GridGraph(3, 3, blocked={(1, 1)}), (0, 0), (2, 2))
    expected_path = ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2))
    # print('预测路径：',result)
    assert result.found is True, f"found={result.found}"
    assert result.path == expected_path, f"path={result.path}"
    assert result.cost == 4, f"cost={result.cost}"
    print("预测正确")
