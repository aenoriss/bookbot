import os

file_path = "books/frankenstein.txt"
file_name = os.path.basename(file_path)


with open(file_path) as f:

    #Get the words from the text
    file_contents = f.read()
    word_arr = file_contents.split()

    #Convert words into lowercase
    word_arr = [word.lower() for word in word_arr]
    
    #Dictionary
    chars = {}

    #Count chars
    for word in word_arr:
        for char in word:
            if char not in chars and char.isalpha():
                chars[char] = 1
            elif char.isalpha():
                chars[char] += 1


    print(f"--- Begin report of books/{file_name} ---")
    print(f"{len(word_arr)} words found in the document")


    for char, count in sorted(chars.items()):
        print(f"The '{char}' character was found {count} times")

    print(sorted(chars.items()))
