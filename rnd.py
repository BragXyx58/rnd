from tkinter import *
import random

def generate_random_number():
    random_number = random.randint(1, 100)
    result.config(text=f"Случайное число: {random_number}")

root = Tk()
root.geometry("200x200")
root.title("Генератор случайных чисел")
button_generate = Button(root, text="Сгенерировать число", command=generate_random_number)
button_generate.pack()
result = Label(root, text="Случайное число: ")
result.pack()
root.mainloop()