with open("books/frankenstein.txt") as f:
    book_text = f.read()
    
def count_words(book_text):
    
    words = book_text.split()
    word_count = len(words)

    return word_count

def count_chars(book_text):
    char_count = {}
    
    for i in book_text:
        lowered_char = i.lower()
        
        if lowered_char.isalpha():
            if lowered_char in char_count:
                char_count[lowered_char] += 1
            else:
                char_count[lowered_char] = 1

    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dict(char_count):
    sorted_list = [{'char': key, 'count': value} for key, value in char_count.items()]
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

def print_report(sorted_chars, word_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for char_dict in sorted_chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report ---")

word_count = count_words(book_text)
char_count = count_chars(book_text)
sorted_chars = sort_dict(char_count)
print_report(sorted_chars, word_count)