class MnM:
    """ This is a class that represents an M&M. Don't modify it. """

    def __init__(self, color):
        """ Create an M&M with the specified color. """
        self.color = color
        self.flavor = "Chocolate"


def find_green_candy_pos(candy_list):
    # Write your code below this comment
    i = 0
    while i < len(candy_list) and candy_list[i].color != "Green":
        i += 1
    if i == len(candy_list):
        return None
    else:
        return i
    # Write your code above this comment


# These are some test cases
def test_1():
    candy_list = []
    candy_list.append(MnM("Red"))
    candy_list.append(MnM("Yellow"))
    candy_list.append(MnM("Blue"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Brown"))
    result = find_green_candy_pos(candy_list)
    print("Test 1, should be 3: ", result)


def test_2():
    candy_list = []
    candy_list.append(MnM("Red"))
    candy_list.append(MnM("Yellow"))
    candy_list.append(MnM("Blue"))
    candy_list.append(MnM("Yellow"))
    candy_list.append(MnM("Brown"))
    result = find_green_candy_pos(candy_list)
    print("Test 2, should be None: ", result)


test_1()
test_2()