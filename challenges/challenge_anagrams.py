def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    word_one, word_two = first_string.lower(), second_string.lower()
    word_one_list = [letter for letter in word_one]
    word_two_list = [letter for letter in word_two]
    word_divider(word_one_list, 0, len(word_one_list) - 1)
    word_divider(word_two_list, 0, len(word_two_list) - 1)
    is_anagram = word_one_list == word_two_list
    if first_string == "" or second_string == "":
        is_anagram = False
    return ("".join(word_one_list), "".join(word_two_list), is_anagram)


def word_divider(word_list, start, end):
    if start < end:
        base = pivot_define(word_list, start, end)
        word_divider(word_list, start, base - 1)
        word_divider(word_list, base + 1, end)


def pivot_define(list, start, end):
    pivot = list[end]
    delimiter = start - 1

    for index in range(start, end):
        if list[index] <= pivot:
            delimiter += 1
            list[index], list[delimiter] = list[delimiter], list[index]
        list[delimiter + 1], list[end] = list[end], list[delimiter + 1]
    return delimiter + 1
