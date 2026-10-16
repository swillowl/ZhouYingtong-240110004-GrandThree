"""M2 lesson 9: quicksort for equipment.

Implement ``quicksort_by`` yourself. Do not call ``sorted()``, ``list.sort()``
or any library sort.

Requirements:

* return a **new** list; never modify ``items``;
* ascending by ``key(item)``; ``descending=True`` gives the reverse order;
* pick the pivot with a rule that does **not** degrade on already-sorted input
  (median-of-three recommended: the median of ``low`` / ``mid`` / ``high``),
  and write your pivot rule in this docstring;
* quicksort is not stable; equal keys may come out in any order.

Events (``source=SOURCE``), one round of partitioning emits, in this order:

* ``partition``    the range being split (e.g. ``low``, ``high``, ``depth``)
* ``pivot``        the chosen pivot (e.g. ``pivot_index``, ``pivot_key``)
* ``compare``      every element compared against the pivot
* ``swap``         every exchange of two different positions
* ``place_pivot``  where the pivot finally lands

Pivot rule: TODO 写下你的枢轴规则
"""

from __future__ import annotations

from typing import Any, Callable, Sequence, TypeVar

from herodungeon.core.events import EventRecorder

T = TypeVar("T")
SOURCE = "m2.quicksort"


def quicksort_by(
    items: Sequence[T],
    key: Callable[[T], Any],
    recorder: EventRecorder | None = None,
    descending: bool = False,
) -> list[T]:
    """Return a new list sorted by ``key`` using quicksort."""
    # TODO: 复制一份 items，在副本上原地排序
    # TODO: 选枢轴（推荐三数取中），emit partition / pivot
    # TODO: 划分：每次与枢轴比较 emit compare，交换 emit swap
    # TODO: 枢轴归位 emit place_pivot，再分别处理左右两段
    # TODO: descending=True 时把比较方向反过来
    #raise NotImplementedError("implement quicksort_by")
    if recorder is None:
        recorder = EventRecorder()

    arr = list(items) 

    def before(a: T, b: T) -> bool:
        return key(a) > key(b) if descending else key(a) < key(b)

    def partition(low: int, high: int, depth: int) -> int:
        recorder.emit("partition", SOURCE, low=low, high=high, depth=depth)

        # 三数取中
        mid = (low + high) // 2
        a, b, c = low, mid, high
        if before(arr[b], arr[a]): a, b = b, a
        if before(arr[c], arr[b]): b, c = c, b
        if before(arr[b], arr[a]): a, b = b, a
        pivot_index = b

        recorder.emit("pivot", SOURCE,
                      pivot_index=pivot_index,
                      pivot_key=key(arr[pivot_index]))

        # 枢轴换到 high
        if pivot_index != high:
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            recorder.emit("swap", SOURCE, i=pivot_index, j=high)
            pivot_index = high
        pivot = arr[high]

        store = low
        for i in range(low, high):
            recorder.emit("compare", SOURCE,
                          i=i, pivot_index=pivot_index,
                          value=key(arr[i]), pivot_value=key(pivot))
            if before(arr[i], pivot):
                if i != store:
                    arr[i], arr[store] = arr[store], arr[i]
                    recorder.emit("swap", SOURCE, i=i, j=store)
                store += 1

        if store != high:
            arr[store], arr[high] = arr[high], arr[store]
            recorder.emit("swap", SOURCE, i=store, j=high)
        recorder.emit("place_pivot", SOURCE, index=store)
        return store

    def sort_range(low: int, high: int, depth: int) -> None:
        if low >= high:
            return
        p = partition(low, high, depth)
        sort_range(low, p - 1, depth + 1)
        sort_range(p + 1, high, depth + 1)

    if len(arr) > 1:
        sort_range(0, len(arr) - 1, 0)
    return arr