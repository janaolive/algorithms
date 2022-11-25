def word_sort(string, start, end):
    if start < end:
        p = divider(string, start, end)
        word_sort(string, start, p - 1)
        word_sort(string, p + 1, end)


def divider(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = string[delimiter], string[index]
    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]
    return delimiter + 1


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_string_lower = []
    for letter in first_string:
        first_string_lower.append(letter.lower())

    second_string_lower = []
    for letter in second_string:
        second_string_lower.append(letter.lower())

    word_sort(first_string_lower, 0, len(first_string_lower) - 1)
    word_sort(second_string_lower, 0, len(second_string_lower) - 1)

    first_string_sorted = ''.join(first_string_lower)
    second_string_sorted = ''.join(second_string_lower)

    if (
        first_string_sorted != second_string_sorted or
        first_string_sorted == '' or second_string_sorted == ''
    ):
        return (first_string_sorted, second_string_sorted, False)
    else:
        return (first_string_sorted, second_string_sorted, True)
