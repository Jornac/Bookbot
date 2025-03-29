def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    ltext = text.lower()
    char_counts = {}
    for char in ltext:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def get_sort(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char":char, "count":count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list





    
