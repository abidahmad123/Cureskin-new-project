def reorder_even_entries(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 != 0 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] % 2 == 0:
            left += 1

        if nums[right] % 2 != 0:
            right -= 1

    return nums


nums = [7, 3, 5, 6, 4, 10, 3, 2]
result = reorder_even_entries(nums)
print(result)

def plus_one(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        digit_sum = digits[i] + carry
        digits[i] = digit_sum % 10
        carry = digit_sum // 10

    if carry:
        digits.insert(0, carry)

    return digits

digits = [1, 2, 9]
result = plus_one(digits)
print(result)


