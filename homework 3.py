def increment_integer(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

        if carry == 0:
            break

    if carry == 1:
        digits.insert(0, 1)

    return digits

digits = [1, 2, 9]
result = increment_integer(digits)
print(result)

def even_first(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums

numbers = [7, 3, 5, 6, 4, 10, 3, 2]
reordered = even_first(numbers)
print(reordered)