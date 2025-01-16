def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    words = word_count(text)
    char_counts = characters_count(text)
    char_counts_list = dic_to_list(char_counts)

    # print(char_counts_list)
    char_counts_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    for item in char_counts_list:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report")

def sort_on(dict):
    return dict["num"]

def dic_to_list(dic):
    a_list = []
    for item in dic:
        a_list.append({"char": item, "num": dic[item]})
    
    return a_list

def characters_count(text):
    count_dic = {}
    for c in text:
        c = c.lower()
        if c not in count_dic:
            count_dic[c] = 0
        
        count_dic[c] += 1
    
    return count_dic



def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()