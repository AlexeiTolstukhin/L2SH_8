from tkinter import *


def function():
    surname = entry_1.get()
    name = entry_2.get()
    gender = var.get()
    if gender == 1:
        gender = 'Женский'
    else:
        gender = 'Мужской'
    print(surname, name, gender)


root = Tk()

row = 0

label_0 = Label(root, text='ФОРМА РЕГИСТРАЦИИ', font='times 18')
label_0.grid(row=row, column=0, columnspan=4)

row += 1
label_1 = Label(root, text='Фамилия:', font='arial 14')
label_1.grid(row=row, column=0)

entry_1 = Entry(root, font='arial 14', width=15)
entry_1.grid(row=row, column=1)

label_2 = Label(root, text='  Имя:', font='arial 14')
label_2.grid(row=row, column=2)

entry_2 = Entry(root, font='arial 14', width=10)
entry_2.grid(row=row, column=3)

row += 1

label_3 = Label(root, text='Укажите пол:', font='arial 14')
label_3.grid(row=row, column=0, columnspan=2)

row += 1

var = IntVar()
r_btn_1 = Radiobutton(root, text='Женский', value=1, variable=var)
r_btn_2 = Radiobutton(root, text='Мужской', value=2, variable=var)

r_btn_1.grid(row=row, column=0)
r_btn_2.grid(row=row, column=1)

row += 1
btn = Button(root, text='Зарегистрироваться', command=function)
btn.grid(row=row, column=3)

root.mainloop()
