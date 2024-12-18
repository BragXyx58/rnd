from tkinter import *
from tkinter import ttk,messagebox
import random

def generate_random_number():
    try:
        min_val = int(combo_min.get())
        max_val = int(combo_max.get())
        if min_val > max_val:
            messagebox.showerror("Ошибка", "'ОТ' не может быть больше 'ДО'")
        else:
            random_number = random.randint(min_val, max_val)
            result.config(text=f"Случайное число: {random_number}")
    except ValueError:
        result.config(text="Error")

root = Tk()
root.geometry("300x300")
root.title("Генератор случайных чисел")
Label(root, text="От:").pack()
combo_min = ttk.Combobox(root, values=list(range(0, 101)))
combo_min.pack()
combo_min.set("0")
Label(root, text="До:").pack()
combo_max = ttk.Combobox(root, values=list(range(0, 101)))
combo_max.pack()
combo_max.set("100")
button_generate = Button(root, text="Сгенерировать число", command=generate_random_number)
button_generate.pack()
result = Label(root, text="Случайное число: ")
result.pack()
root.mainloop()
