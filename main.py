from stats import get_wordcount, character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    char_counts = character_counts(text)
    wc = get_wordcount(text)
    print(f"{wc} words found in the document")
    print(char_counts)

main()