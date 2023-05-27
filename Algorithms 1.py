# Part 1 of homework
def sum(n):

    count = 0

    Result = 0

    while count <= n:
        Result += count
        count += 1
        # print(count)

    print(Result)
    return

sum(5)

# Part 2 of homework

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

print("Max value out of [124, 21, 32] is: ", maximum(124, 21, 32))

# Part 3 of homework
def countEvenOdd(n):

    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        else:
            odd_count += 1

        n = int(n / 10)

    print("Even count : ", even_count)
    print("Odd count : ", odd_count)
    if (even_count % 2 == 0 and
            odd_count % 2 != 0):
        return 1
    else:
        return 0

n = 34560;

countEvenOdd(n);