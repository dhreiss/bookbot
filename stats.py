def get_num_words(text):
    return(len(text.split()))

def get_num_chars(text):
    char_count = {}
    for c in "".join(text.split()).lower():
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return(dict(sorted(char_count.items(), key=lambda key: key[1], reverse=True)))
