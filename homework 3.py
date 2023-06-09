def print_reverse(statement):
    words = statement.split()
    reversed_words = list(reversed(words))
    reversed_statement = " ".join(reversed_words)
    print(reversed_statement)

input_statement = "Everything is hard before it is easy"

print_reverse(input_statement)

def print_permutations(string):
    permutations = []

    def generate_permutations(string, start, end):
        if start == end:
            permutations.append("".join(string))
        else:
            for i in range(start, end + 1):
                string[start], string[i] = string[i], string[start]
                generate_permutations(string, start + 1, end)
                string[start], string[i] = string[i], string[start]  # backtrack

    char_list = list(string)
    generate_permutations(char_list, 0, len(char_list) - 1)

    for permutation in permutations:
        print(permutation)

input_string = "ABC"
print_permutations(input_string)

def count_vowels_and_consonants(string):
    vowels = 0
    consonants = 0

    string = string.lower()

    vowel_set = set('aeiou')

    for char in string:
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1

    return {'Vowels': vowels, 'Consonants': consonants}

input_string = "hello world"
result = count_vowels_and_consonants(input_string)
print(result)