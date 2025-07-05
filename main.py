from stats import *
import sys

def main():

    if len(sys.argv) == 2:

        book_file_path = sys.argv[1]

        book_text = get_book_text(book_file_path)
        word_nums = get_word_count(book_text)

        char_nums = get_character_count(book_text)
        sorted_char_nums = sort_dict_chars(char_nums)


        generate_printout(book_file_path,word_nums,sorted_char_nums)

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()