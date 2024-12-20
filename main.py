# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def convert_and_sort(char_counts): #This is taking the char_counts as an argument
    char_list = [{'character': char, 'num': count} for char, count in char_counts.items()]
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def word_count(contents):
    words = contents.split() # create a vaiable and set it to a split of the argument passed to the parameter contents
    count = len(words) # Counts the number of words. Using len(words to set variable count instead of an int like 0.)
    return count

def character_count(text):
    characters = {}
    for char in text: # Converts the characters in the text to lowercase. Which will help handle duplicates of upper and lower instead placing them together
        lowercase_char = char.lower()
        if lowercase_char in characters: # if it exists in dictionary characters, add 1 to the count
            characters[lowercase_char] += 1
        else: #if it doesnt, set the value to 1
            characters[lowercase_char] = 1
    return characters

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        # 'f' is just a variable name that lets us work with the file. It could be anything.
        contents = f.read()
    #print(contents) # This line prints the contents
    total_words = word_count(contents) # Calling the word-counting function
    print(total_words) # Print the word count
    char_counts = character_count(contents)
    sorted_chars = convert_and_sort(char_counts)
    for item in sorted_chars:
        print(f"The '{item['character']}' character was found {item['num']} times")


# need a call to the function so that it actually runs
main()

