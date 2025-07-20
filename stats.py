
def get_wordcount(book):
    words = book.split()
    return len(words)

def character_counts(book):
    char_count = {} #dict
    for char in book:
            lowered = char.lower()

            if lowered in char_count:
                char_count[lowered] += 1
            else:
                char_count[lowered] = 1

    return char_count

def sort_key(items):
     return items["num"]

def sort_dict(dict):
    items = dict.items()
    endlist = []
    for char,num in items:
        endlist.append({"char": char, "num": num})
    
    endlist.sort(reverse=True, key=sort_key)
    return endlist
        
          
          
