def split_and_swap(string):
    length = len(string)
    half_length = length // 2

    first_part = string[:half_length + length % 2]
    second_part = string[half_length + length % 2:]

    result = second_part + first_part

    return result

string = 'bbbbbcaaaaa'
result = split_and_swap(string)
print(result)

def has_unique_characters(string):
    return len(string) == len(set(string))

string1 = 'abcde'
print(has_unique_characters(string1))

string2 = 'aabcde'
print(has_unique_characters(string2))