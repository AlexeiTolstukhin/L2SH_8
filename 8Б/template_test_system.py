from tkinter import *


def import_test(filename='input.txt'):
    test = dict()
    answers = []
    file = open(filename, 'r', encoding='utf8')

    # далее ваш код

    # чтобы сравнить результат с образцом
    print(test)
    print(answers)
    return test, answers
