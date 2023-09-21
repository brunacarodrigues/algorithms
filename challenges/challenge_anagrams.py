# Refatorando por não poder utilizar funções prontas (sort, sorted, Counter)

def quick_sort(string):
    if len(string) <= 1:
        return string

    mid = string[len(string) // 2]
    first = [letter for letter in string if letter.lower() < mid.lower()]
    middle = [letter for letter in string if letter.lower() == mid.lower()]
    second = [letter for letter in string if letter.lower() > mid.lower()]

    return quick_sort(first) + middle + quick_sort(second)


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    first_sorted = ''.join(quick_sort(list(first_string)))
    second_sorted = ''.join(quick_sort(list(second_string)))
    if not first_string or not second_string:
        return (first_sorted, second_sorted, False)

    return (first_sorted, second_sorted, first_sorted == second_sorted)
