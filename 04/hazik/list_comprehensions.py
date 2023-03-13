#!/usr/bin/env python3


def ex_1():
    print("\nFIRST EXERCISE\n")
    words = ["auto", "villamos", "metro"]
    result = [word.upper() + "!" for word in words]
    print(words, end="")
    print(" --> ", end="")
    print(result)


def ex_2():
    print("\nSECOND EXERCISE\n")
    words = ['aladar', 'bela', 'cecil']
    result = [word.capitalize() for word in words]
    print(words, end="")
    print(" --> ", end="")
    print(result)


def ex_3():
    print("\nTHIRD EXERCISE\n")
    result = [0 for i in range(0, 9+1)]
    print(result)


def ex_4():
    print("\nFOURTH EXERCISE\n")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = [n*2 for n in nums]
    print(nums, end="")
    print(" --> ", end="")
    print(result)


def ex_5():
    print("\nFIFTH EXERCISE\n")
    str_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result = [int(n) for n in str_nums]
    print(str_nums, end="")
    print(" --> ", end="")
    print(result)


def ex_6():
    print("\nSIXTH EXERCISE\n")
    merged = "1234567"
    joined = " ".join(merged)
    splitted = joined.split(" ")

    result = [int(n) for n in splitted]
    print(merged, end="")
    print(" --> ", end="")
    print(result)


def ex_7():
    print("\nSEVENTH EXERCISE\n")
    sentence = "The quick brown fox jumps over the lazy dog"
    splitted = sentence.split(" ")
    result = [len(word) for word in splitted]
    print(sentence, end="")
    print(" --> ", end="")
    print(result)


def ex_8():
    print("\nEIGHTH EXERCISE\n")
    sentence = "python is an awesome language"
    splitted = sentence.split(" ")
    result = [word[0] for word in splitted]
    print(sentence, end="")
    print(" --> ", end="")
    print(result)


def ex_9():
    print("\nNINTH EXERCISE\n")
    sentence = "The quick brown fox jumps over the lazy dog"
    splitted = sentence.split(" ")
    result = [(word, len(word)) for word in splitted]
    print(sentence, end="")
    print(" --> ", end="")
    print(result)


def ex_10():
    print("\nTENTH EXERCISE\n")
    result = [num for num in range(0,9+1) if num % 2 == 0]
    print(result)


def ex_11():
    print("\nELEVENTH EXERCISE\n")
    result = [num*num for num in range(0,19+1) if num*num % 2 == 0]
    to_string = [str(e) for e in result]
    result = [e for e in to_string if e[-1] == '4']
    print(result)


def ex_12():
    print("\nTWELFTH EXERCISE\n")
    nums = [num*num for num in range(0,19+1)]
    print(nums)


def ex_13():
    print("\nTHIRTEENTH EXERCISE\n")
    letters = [chr(l) for l in range(65, 90+1)]
    result = "".join(letters)
    print(letters, end="")
    print(" --> ", end="")
    print(result)


def ex_14():
    print("\nFOURTEENTH EXERCISE\n")
    elements = [' apple ', ' banana ', ' kiwi']
    result = [element.strip() for element in elements]
    print(elements, end="")
    print(" --> ", end="")
    print(result)


def ex_15():
    print("\nFIFTEENTH EXERCISE\n")
    nums = [1, 0, 1, 1, 0, 1, 0, 0]
    to_string = [str(n) for n in nums]
    result = "".join(to_string)
    print(nums, end="")
    print(" --> ", end="")
    print(result)


def main():
    ex_1()
    print('\n', '-' * 80)
    ex_2()
    print('\n', '-' * 80)
    ex_3()
    print('\n', '-' * 80)
    ex_4()
    print('\n', '-' * 80)
    ex_5()
    print('\n', '-' * 80)
    ex_6()
    print('\n', '-' * 80)
    ex_7()
    print('\n', '-' * 80)
    ex_8()
    print('\n', '-' * 80)
    ex_9()
    print('\n', '-' * 80)
    ex_10()
    print('\n', '-' * 80)
    ex_11()
    print('\n', '-' * 80)
    ex_12()
    print('\n', '-' * 80)
    ex_13()
    print('\n', '-' * 80)
    ex_14()
    print('\n', '-' * 80)
    ex_15()
    print('\n', '-' * 80)


if __name__ == "__main__":
    main()