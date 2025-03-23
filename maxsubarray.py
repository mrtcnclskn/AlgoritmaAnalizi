def max_subarray_sum(arr):
    def helper(low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2
        left_max = helper(low, mid)
        right_max = helper(mid + 1, high)
        cross_max = max_crossing_sum(low, mid, high)

        return max(left_max, right_max, cross_max)

    def max_crossing_sum(low, mid, high):
        left_sum, total = float('-inf'), 0
        for i in range(mid, low - 1, -1):
            total += arr[i]
            left_sum = max(left_sum, total)

        right_sum, total = float('-inf'), 0
        for i in range(mid + 1, high + 1):
            total += arr[i]
            right_sum = max(right_sum, total)

        return left_sum + right_sum

    return helper(0, len(arr) - 1)

def max_subarray(nums):
    max_sum, current_sum = nums[0], nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
