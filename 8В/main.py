from tkinter import *


def import_text(filename='input.txt'):
    file = open(filename, 'r', encoding='utf8')
    test = dict()
    answers = []
    # далее ваш код
    print(test)  # чтобы свериться с заданием
    print(answers)  # чтобы свериться с заданием
    return test, answers


def finish_test():
    family = surname.get()
    nick = name.get()
    ans1 = answer1.get()
    ans2 = answer2.get()
    print(family, nick, ans1, ans2)


root = Tk()

label_0 = Label(root, text='Введите фамилию и имя')
label_0.grid(row=0, column=0, columnspan=2)

label_1 = Label(root, text='Фамилия:')
label_1.grid(row=1, column=0)

surname = Entry(root)
surname.grid(row=1, column=1)

label_2 = Label(root, text='   Имя:')
label_2.grid(row=1, column=2)

name = Entry(root)
name.grid(row=1, column=3)

label_3 = Label(root, text='Вопрос номер 1')
answer1 = IntVar()
r_btn_1 = Radiobutton(root, text='Ответ 1', variable=answer1, value=1)
r_btn_2 = Radiobutton(root, text='Ответ 2', variable=answer1, value=2)
label_3.grid(row=2, column=0, columnspan=4)
r_btn_1.grid(row=3, column=0, columnspan=4)
r_btn_2.grid(row=4, column=0, columnspan=4)

label_4 = Label(root, text='Вопрос номер 2')
answer2 = IntVar()
r_btn_41 = Radiobutton(root, text='Ответ 1', variable=answer2, value=41)
r_btn_42 = Radiobutton(root, text='Ответ 2', variable=answer2, value=42)
label_4.grid(row=5, column=0, columnspan=4)
r_btn_41.grid(row=6, column=0, columnspan=4)
r_btn_42.grid(row=7, column=0, columnspan=4)

btn = Button(root, text="Закончить", command=finish_test)
btn.grid(row=2, column=3)

root.mainloop()
