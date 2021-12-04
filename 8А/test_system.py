from tkinter import *


def check():
    for i in range(len(user_answers)):
        print(user_answers[i].get())


font_header = 'arial 14'
font_text = 'arial 12'

root = Tk()

row = 0

label = Label(root, text='ТЕСТИРУЮЩАЯ СИСТЕМА', font=font_header)
label.grid(row=row, column=0)

row += 1

test = {
    'Вопрос 1': ['Ответ 11', 'Ответ 12', 'Ответ 13'],
    'Вопрос 2': ['Ответ 21', 'Ответ 22', 'Ответ 23'],
    'Вопрос 3': ['Ответ 31', 'Ответ 32', 'Ответ 33'],
    'Вопрос 4': ['Ответ 41', 'Ответ 42', 'Ответ 43']
}

user_answers = [IntVar() for i in range(len(test))]

n_question = 1
for question in test:
    row += 1
    label_question_1 = Label(root, text=question, font=font_text)
    label_question_1.grid(row=row, column=0)

    r_btn_1 = Radiobutton(root, text=test[question][0],
                          value=n_question * 10 + 1,
                          variable=user_answers[n_question - 1])
    r_btn_2 = Radiobutton(root, text=test[question][1],
                          value=n_question * 10 + 2,
                          variable=user_answers[n_question - 1])
    r_btn_3 = Radiobutton(root, text=test[question][2],
                          value=n_question * 10 + 3,
                          variable=user_answers[n_question - 1])
    row += 1
    r_btn_1.grid(row=row, column=0)
    row += 1
    r_btn_2.grid(row=row, column=0)
    row += 1
    r_btn_3.grid(row=row, column=0)
    n_question += 1

row += 1
btn = Button(root, text='Стоп! Хватит!', font=font_text, command=check)
btn.grid(row=row, column=0)

root.mainloop()
