def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_on(item):
    return item["num"]


def sort_characters(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list