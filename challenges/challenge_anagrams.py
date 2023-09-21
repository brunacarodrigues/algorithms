def is_anagrams(first_string, second_string):
    def count_characters(word):
        char_count = {}
        for char in word:
            if char.isalpha():
                char = char.lower()
                char_count[char] = char_count.get(char, 0) + 1
        return char_count

    first_count = count_characters(first_string)
    second_count = count_characters(second_string)

    return first_count == second_count
