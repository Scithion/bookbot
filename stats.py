import sys

def get_book_text(book):
    file_contents=book.read()
    return file_contents

def get_num_words():
    with open(sys.argv[1]) as book:
        t=get_book_text(book)
        components = []
        components =t.split()
        count=0
        count = len(components)
        # for words in components:
        #    count +=1
        
        # print(f"{count} words found in the document")  # Optional: print the word count
        return count

def get_num_letters():
    with open(sys.argv[1]) as book:
        t=get_book_text(book)
        alphabet = {}
        for word in t:
            characters = list(word)
            for character in characters:
                if character.isalpha():
                    character = character.lower()
                    if character in alphabet:
                        alphabet[character] += 1
                    else:
                        alphabet[character] = 1
    return alphabet


def format_alphabet(alphabet_input):
    X = []
    for key in alphabet_input:
        letter_entry={}
        letter_entry["character"]=key
        letter_entry["count"]=alphabet_input[key]
        X.append(letter_entry)
    return X

def sort_on(letter_entry):
    return letter_entry["count"]

def sort_alphabet():
    F = format_alphabet(get_num_letters())
    F.sort(key=sort_on, reverse=True)
    return F


def report():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    # print(get_num_letters()) # debug
    twinkle = sort_alphabet()
    for letter_dict in twinkle:
        print(f"{letter_dict['character']}: {letter_dict['count']}")
    print("============= END ===============")