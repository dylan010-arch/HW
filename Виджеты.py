#1
import tkinter as tk

def show_info():
    result_label.config(text=f"Имя: {name_entry.get()} \n Возраст: {age_entry.get()} \n Город: {city_entry.get()}")

root = tk.Tk()
root.title("Информация обо мне")

name_label = tk.Label(root, text="Имя:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_label = tk.Label(root, text="Возраст:")
age_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = tk.Label(root, text="Город:")
city_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
city_entry = tk.Entry(root)
city_entry.grid(row=2, column=1, padx=10, pady=10)

info_button = tk.Button(root, text="Показать информацию", command=show_info)
info_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)
root.mainloop()

#2
import tkinter as tk
from tkinter import scrolledtext

def update_text():
    entered_text = entry.get()
    text_area.delete(1.0, tk.END)  
    text_area.insert(tk.END, entered_text) 

root = tk.Tk()
root.title("Текстовый интерфейс")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_area.pack(pady=20)

update_button = tk.Button(root, text="Обновить текст", command=update_text)
update_button.pack(pady=20)

root.mainloop()
