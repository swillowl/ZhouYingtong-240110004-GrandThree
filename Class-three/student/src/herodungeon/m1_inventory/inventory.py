"""M1 lesson 3: implement the list-based inventory.

Replace every `NotImplementedError` below. Do not change the public method
names or the exception types — the tests depend on them.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from herodungeon.core.events import AlgorithmEvent, EventRecorder
from herodungeon.core.models import Item


class InventoryFullError(ValueError):
    pass


class ItemNotFoundError(KeyError):
    pass

@dataclass(slots=True)
class Inventory:
    capacity: int
    recorder: EventRecorder = field(default_factory=EventRecorder)
    _items: list[Item] = field(default_factory=list, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.capacity <= 0:
            raise ValueError("capacity must be positive")

    @property
    def items(self) -> tuple[Item, ...]:
        return tuple(self._items)

    def add(self, item: Item) -> AlgorithmEvent:
        """Append `item` if there is room; otherwise reject and raise."""
        # TODO: 背包满时 emit reject 并抛出 InventoryFullError
        # TODO: item_id 重复时抛出 ValueError
        # TODO: 追加物品并 emit insert
        if len(self._items) >= self.capacity:
            event = self.recorder.emit("reject", "Inventory.add", item_id=item.item_id)
            raise InventoryFullError(f"Cannot add item {item.item_id}: inventory is full.") 
        if any(item.item_id == existing.item_id for existing in self._items):
            raise ValueError(f"Item with ID {item.item_id} already exists in inventory.")
        self._items.append(item)
        event = self.recorder.emit("insert", "Inventory.add", item_id=item.item_id)
        return event
        #raise NotImplementedError("implement Inventory.add")

    def remove(self, item_id: str) -> Item:
        """Find `item_id` from the front, emit compare/remove/miss, and return it."""
        # TODO: 逐个 compare
        # TODO: 找到后 pop，emit remove，返回该物品
        # TODO: 找不到时 emit miss 并抛出 ItemNotFoundError
        for index, item in enumerate(self._items):
            self.recorder.emit("compare", "Inventory.remove", item_id=item.item_id)
            if item.item_id == item_id:
                removed_item = self._items.pop(index)
                self.recorder.emit("remove", "Inventory.remove", item_id=removed_item.item_id)
                return removed_item
        self.recorder.emit("miss", "Inventory.remove", item_id=item_id)
        raise ItemNotFoundError(f"Item with ID {item_id} not found in inventory.")      
        #raise NotImplementedError("implement Inventory.remove") 

    def total_value(self) -> int:
        """Return the sum of item values currently in the bag."""
        # TODO: 返回所有物品 value 之和
        return sum(item.value for item in self._items)
        #raise NotImplementedError("implement Inventory.total_value")
