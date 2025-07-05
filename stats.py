def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def get_word_count(file_text):
    split_words = file_text.split()
    return len(split_words)


def get_character_count(file_text):
    file_text = file_text.lower()
    char_dict = {}

    for char in file_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    #print(f"char_dict : {char_dict}")
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict_chars(dict_chars):
    list_chars = []

    for char in dict_chars:
        #print(f"char : {char}")
        #print(f"dict_chars[char] : {dict_chars[char]}")
        list_chars.append({"name": char, "num" : dict_chars[char]})

    list_chars.sort(reverse=True, key=sort_on)

    #print(f"dict_chars : {dict_chars}")
    #print(f"list_chars : {list_chars}")
    return list_chars


def generate_printout(book_file_path, word_nums, sorted_char_nums):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_nums} total words")
    print("--------- Character Count -------")

    for char in sorted_char_nums:
        if char['name'].isalpha():
            print(f"{char['name']}: {char['num']}")
        
    print("============= END ===============")