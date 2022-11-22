def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if word == '':
        return False
    elif len(word) == 1:
        return True
    elif high_index > low_index:
        return (
            word[low_index] == word[high_index]
            and is_palindrome_recursive(word, low_index + 1, high_index - 1)
        )

    return True
