def get_num_words(contents: str):
    return len(contents.split())

def get_character_count(contents: str):
    counts = {}
    for char in contents:
        char = char.lower()
        counts.setdefault(char, 0)
        counts[char] = counts[char] + 1
    return counts

def sort_chars(char_count: dict):
    def sort_on(d: dict):
        return d["count"]

    l = []
    for k, v in char_count.items():
        l.append({"char": k, "count": v})
    l.sort(reverse=True, key=sort_on)
    return l
