def print_words(letters):

    # Search for words containing the combination
    with open("dictionary.txt", "r") as file:
        words = file.read().splitlines()

    # Print words containing the random combination
    matching_words = [word for word in words if letters in word]
    for word in matching_words:
        print(word)

def check_word(word):
    with open("dictionary.txt", "r") as file:
        for line in file:
            if line.strip() == word.upper():
                print("Word is Valid!")
                return
        print("Word is not valid!")

# Example usage

print_words("VR")                   # Returns all valid words containing input substring
check_word("Vroom")                 # Checks if input word is actually a word