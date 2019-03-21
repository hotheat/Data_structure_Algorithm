"""
利用归并排序返回数组中的逆序对数
"""

inverse_num = 0


def inverse_count(nums):
    return merge_sort_counting(nums, 0, len(nums) - 1)


def merge_sort_counting(nums, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort_counting(nums, start, mid)
    merge_sort_counting(nums, mid + 1, end)
    merge(nums, start, mid, end)


def merge(nums, start, mid, end):
    global inverse_num
    tmp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            # 统计 i 到 end 之间比 nums[j] 大的元素个数
            inverse_num += mid - i + 1
            tmp.append(nums[j])
            j += 1

    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= end:
        tmp.append(nums[j])
        j += 1

    nums[start:end + 1] = tmp


if __name__ == '__main__':
    nums = [5, 3, 2, 1, 4]
    inverse_count(nums)
    print(nums)
    print(inverse_num)
