def on_sort(items):
    return items["num"]

def get_num_of_words(text: str):
    words = text.split()
    return len(words)

def count_characters(text: str):
    text = text.lower()
    count = {}
    for c in text:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

def to_sorted_list(count: dict):
    unsorted_list = []
    for entry in count:
        unsorted_list.append({"char": entry, "num": count[entry]})
    
    unsorted_list.sort(key=on_sort, reverse=True)
    return unsorted_list