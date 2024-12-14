from tkinter import *
import random

# Переменные
count = 0
random_num = random.randint(1, 100)
num = None
otvet=None
def clicked():
    lbl_start.config(text=f"Количество попыток: {count}")

def guess():
    global count
    global num
    global otvet
    count += 1

    num = int(txt.get())  # Преобразуем ввод в целое число
    if num>random_num:
        otvet=("число компьютера меньше")
    if num<random_num:
            otvet=('число компьютера больше')
    if num==random_num:
            otvet=('Вы угадали! поздравляем')
    lbl_guesses.config(text=f"Введенное число: {num}\n {otvet}")
    lbl_start.config(text=f"Количество попыток: {count}")
    txt.delete(0, END)


def reset():
      global count
      global random_num
      global otvet
      count=0
      random_num=random.randint(1,100)
      otvet=(' ')
      lbl_start.config(text=f"Количество попыток: {count}")
      btn_start = Button(window, text="Начать", command=clicked)
      lbl_guesses.config(text='')
      
# Создаем окно
window = Tk()
window.title("Угадай число")
window.geometry('400x300')

# Метка приветствия
lbl_start = Label(window, text="Привет! Ваша задача угадать число от 1 до 100,\n которое выбрал компьютер.", font=("Arial Bold", 10))
lbl_start.pack(pady=(10, 0))

# Кнопка начала игры
btn_start = Button(window, text="Начать", command=clicked)
btn_start.pack(pady=(10, 0))

# Поле ввода
txt = Entry(window, width=20)
txt.pack(pady=(30, 0))

# Кнопка для ввода числа
btn_guess = Button(window, text="Ввести число", command=guess)
btn_guess.pack(pady=(10, 0))

# Метка для вывода количества попыток и введенных чисел
lbl_guesses = Label(window, text="", font=("Arial", 12))
lbl_guesses.pack(pady=(10, 0))
# Кнопка сброса
btn_reset = Button(window, text="начать заного", font=("Arial", 12),command=reset)
btn_reset.pack(pady=(10,0))
# Запуск главного цикла
window.mainloop()