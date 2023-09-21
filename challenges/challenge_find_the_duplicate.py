def find_duplicate(nums):
    if len(nums) < 2:
        return False

    nums.sort()
    seen = set()

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in seen:
            return num
        seen.add(num)

    return False
