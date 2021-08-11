def longest(list1=None):
    if list1 is None:
        list1 = ["the", "quick", "brown", "fox", "ate", "my", "chickens"]
    longest_word = ""
    counter = 0
    while True:
        for long in list1:
            if len(longest_word) == len(long):
                counter += 1

        if counter > 1:
            for long in list1:
                if len(longest_word) == len(long):
                    print(long)
            break

        for long in list1:
            if len(long) > len(longest_word):
                longest_word = long
        if counter == 1:
            print(longest_word)
            break
