def get_num_words(text):
    return len(text.split())


def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(item):
    return item["num"]


def sorted_character_counts(char_counts):
    sorted_characters = []

    for char in char_counts:
        if char.isalpha():
            sorted_characters.append({
                "char": char,
                "num": char_counts[char]
            })

    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
