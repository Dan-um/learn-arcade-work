import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def main():
    my_file = open("dictionary.txt")

    dictionary_list = []

    for line in my_file:
        line = line.strip()

        dictionary_list.append(line)

    my_file.close()

    print("There were", len(dictionary_list), "Words in the file.")

    print("---Linear Search---")
    my_file2 = open("AliceInWonderLand200.txt")
    for  in my_file2:
        word_list = split_line(line)




main()