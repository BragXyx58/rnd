from tkinter import *
from tkinter import ttk, messagebox
import random


def generate_random_number():
    try:
        min_val = int(num_min.get())
        max_val = int(num_max.get())
        if min_val > max_val:
            messagebox.showerror("Ошибка", "'ОТ' не может быть больше 'ДО'")
        else:
            random_number = random.randint(min_val, max_val)
            exceptions = [int(item) for item in list_exceptions.get(0, END)]
            while random_number in exceptions:
                random_number = random.randint(min_val, max_val)

            result.config(text=f"Случайное число: {random_number}")
    except ValueError:
        result.config(text="Ошибка ввода")


def add_exception():
    try:
        exception = int(entry_exception.get())
        list_exceptions.insert(END, exception)
        entry_exception.delete(0, END)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")


root = Tk()
root.geometry("300x400")
root.title("Генератор случайных чисел")
Label(root, text="От:").pack()
num_min = ttk.Combobox(root, values=list(range(0, 101)))
num_min.pack()
num_min.set("0")
Label(root, text="До:").pack()
num_max = ttk.Combobox(root, values=list(range(0, 101)))
num_max.pack()
num_max.set("100")
Label(root, text="Исключения:").pack()
entry_exception = Entry(root)
entry_exception.pack()
button_add_exception = Button(root, text="Добавить исключение", command=add_exception)
button_add_exception.pack(pady=5)
list_exceptions = Listbox(root)
list_exceptions.pack(pady=5)
button_generate = Button(root, text="Сгенерировать число", command=generate_random_number)
button_generate.pack(pady=10)
result = Label(root, text="Случайное число: ")
result.pack()
root.mainloop()
