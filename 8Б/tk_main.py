from tkinter import *


def finish():
    print(var.get())
    print(text_fio.get())


root = Tk()

btn_click = Button(root, command=finish, text='Закончить', width=10, height=2, bg='yellow', fg='black')
btn_click.grid(row=1, column=1)

text_fio = Entry(root)
text_fio.grid(row=0, column=0, columnspan=2)

lbl_question_1 = Label(root, text='Ваш вопрос')
lbl_question_1.grid(row=1, column=0)

var = IntVar()
rbutton1 = Radiobutton(root, text='1', variable=var, value=1)
rbutton2 = Radiobutton(root, text='2', variable=var, value=2)
rbutton3 = Radiobutton(root, text='3', variable=var, value=3)
rbutton1.grid(row=2, column=0)
rbutton2.grid(row=3, column=0)
rbutton3.grid(row=4, column=0)

root.mainloop()
