from tkinter import *


def check():
    global row
    r = 0
    a1 = answer_1.get()
    a2 = answer_2.get()
    if a1 == 11:
        r += 1
    if a2 == 23:
        r += 1
    label = Label(root, text=f'Поздравляем! У Вас - {r} балла из 2.')
    label.grid(row=row + 1, column=0)


font_header = 'arial 14'
font_text = 'arial 12'

root = Tk()

row = 0

label = Label(root, text='ТЕСТИРУЮЩАЯ СИСТЕМА', font=font_header)
label.grid(row=row, column=0)

row += 1

label_question_1 = Label(root, text='Вопрос 1', font=font_text)
label_question_1.grid(row=row, column=0)
row += 1
answer_1 = IntVar()
r_btn_1 = Radiobutton(root, text='Ответ 1', value=11, variable=answer_1)
r_btn_2 = Radiobutton(root, text='Ответ 2', value=12, variable=answer_1)
r_btn_3 = Radiobutton(root, text='Ответ 3', value=13, variable=answer_1)
row += 1
r_btn_1.grid(row=row, column=0)
row += 1
r_btn_2.grid(row=row, column=0)
row += 1
r_btn_3.grid(row=row, column=0)

row += 1
label_question_2 = Label(root, text='Вопрос 2', font=font_text)
label_question_2.grid(row=row, column=0)

row += 1
answer_2 = IntVar()
r_btn_1 = Radiobutton(root, text='Ответ 1', value=21, variable=answer_2)
r_btn_2 = Radiobutton(root, text='Ответ 2', value=22, variable=answer_2)
r_btn_3 = Radiobutton(root, text='Ответ 3', value=23, variable=answer_2)
row += 1
r_btn_1.grid(row=row, column=0)
row += 1
r_btn_2.grid(row=row, column=0)
row += 1
r_btn_3.grid(row=row, column=0)

row += 1
btn = Button(root, text='Стоп! Хватит!', font=font_text, command=check)
btn.grid(row=row, column=0)

root.mainloop()
