def count_words():
    words_counter = 0
    with open("books/frankenstein.txt") as f:
        data = f.read()
        lines = data.split()
        words_counter += len(data.split())
    print(words_counter, "words found in the document")
count_words()
def letters_count():
    char_count = {}
    with open("books/frankenstein.txt") as f:
        text = f.read()
        lowered_char = text.lower()
        for char in lowered_char:
            if char.isalpha():
                char_count[char] = char_count.get(char, 0) + 1
    return char_count
result = letters_count()
sorted_items = sorted(result.items())
for char, count in sorted_items:
    def sort_on(result):
        list_of_dicts = [{"letter": char, "count": count} for char, count in result.items()]
        sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: x["letter"])
        return sorted_list_of_dicts
sorted_result = sort_on(result)
for entry in sorted_result:
    print(f"The, {entry['letter']} character was found, {entry['count']} times")
print("---End report---")
