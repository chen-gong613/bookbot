def get_num_words(path):
    list = get_book_text(path).split()
    num_words = len(list)
    print(f"Found {num_words} total words")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()    

def get_num_char(path):
    counter = {}
    string = get_book_text(path)

    for i in string:
        if i.isalpha():
            i = i.lower()
            if i in counter:
                counter[i] +=1
            else:
                counter[i] = 1
    return counter

def get_count(dt):
    return dt["num"]

def sort_dict(counter_dict):
    # Convert to list of dicts with keys "char" and "num"
    kv_list = [{"char": k, "num": v} for k, v in counter_dict.items() if k.isalpha()]
    
    # Sort in-place by "num" from largest to smallest
    kv_list.sort(key=get_count, reverse=True)

    return kv_list