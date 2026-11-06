from monster_ai import is_hp_low, is_hero_in_sight, attack, BehaviorStatus

# 把低血阈值改成 50%。当前10点，满血20点：比例刚好是 50%。  
world1 = {"monster_hp": 10, "monster_max_hp": 20, "hp_threshold": 0.5}
world2 = {"hero_pos": (5, 5),"monster_pos": (5,6), "sight_range": 5}
world3 = {"attack_cooldown": 0, "hero_hp": 20, "damage": 5, "cooldown": 4}

# 先写下你的预测：刚好等于阈值，算低血吗？
assert is_hp_low(world1) is False, "10/20 刚好是50%，不是“低于”50%"
assert is_hero_in_sight(world2) is True, "勇者在范围内"
assert attack(world3) == BehaviorStatus.SUCCESS, "攻击应该成功"
print("我的测试通过")