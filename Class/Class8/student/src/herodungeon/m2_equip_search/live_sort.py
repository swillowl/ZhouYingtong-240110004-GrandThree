"""第 8 次课当场写的快排和精确二分。

四个函数都还是空的，会抛 NotImplementedError。请只改这个文件。
本课排的是一串整数。装备上的 quicksort_by 在第 9 课写。
左边界（第一个大于等于）在第 10 课写，这里不要写。
"""

from __future__ import annotations


def partition(nums: list[int]) -> tuple[list[int], int, list[int]]:
    """取当前这一段的第一个数当基准。

    比基准小的按遇到的顺序放左，大于或等于基准的按遇到的顺序放右。
    返回 (左堆, 基准, 右堆)。nums 至少有一个数。
    """
    # TODO: 基准 = nums[0]
    # TODO: 其余的数，小的进左，不比它小的进右，保持原来的先后
    pivot = nums[0]
    left = []
    right = []
    for n in nums[1:]:
        if n < pivot:
            left.append(n)
        else:
            right.append(n)
    return left, pivot, right


def quicksort(nums: list[int]) -> list[int]:
    """用 partition 把左右两堆排完。只剩 0 个或 1 个数时停下来。

    返回排好的新列表即可，不必改调用者手里的那份。
    """
    # TODO: 长度 <= 1 时直接返回一份拷贝
    # TODO: 否则 partition，再把「排好的左堆 + 基准 + 排好的右堆」接起来
    if len(nums) <= 1:
        return nums[:]
    left, pivot, right = partition(nums)
    return quicksort(left) + [pivot] + quicksort(right)



def binary_search(nums: list[int], target: int) -> int:
    """在已经排好的列表里做精确匹配。找到返回下标，找不到返回 -1。

    不要写第 10 课那种「第一个大于等于」的缩区间。
    """
    # TODO: lo、hi 包住还没看过的下标；mid 取中间
    # TODO: 相等就返回 mid；目标更大就往右，更小就往左
    # TODO: 区间空了返回 -1
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def count_at_least(sorted_nums: list[int], threshold: int) -> int:
    """sorted_nums 已经从小到大排好。数有多少个 >= threshold。

    从第一个够格的数开始往后数即可。不要写左边界那套 ans / 缩区间。
    """
    # TODO: 找到第一个 >= threshold 的位置，它和它右边的都算
    count = 0
    for num in sorted_nums:
        if num >= threshold:
            count += 1
    return count

