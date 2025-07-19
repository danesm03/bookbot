from stats import get_wordcount
    
def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    print(f"{get_wordcount(text)} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()