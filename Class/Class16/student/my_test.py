from copy import deepcopy
from lesson16_practice import reconstruct_items
from lesson_data import ITEMS, TABLE

#选取前3个包，传入4行表格，限重5公斤，看看能带走哪些包
chosen = reconstruct_items(ITEMS[:3], deepcopy(TABLE[:4]), 5)
ids = [item.item_id for item in chosen]
# print(f"DEBUG: 实际选中的物品是: {ids}") 
assert sorted(ids) == ["a", "b"], "限重5公斤可以带A和B"
print("我的测试通过", ids)