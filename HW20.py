#1
import tkinter as tk

def on_pressed(event):
    text = entry.get()
    label.config(text="Текст:" + text)

window = tk.Tk()
window.geometry("400x400")

entry = tk.Entry(window, font=("Arial", 12), fg="black")
entry.pack()
entry.bind("<Return>", on_pressed)

label = tk.Label(window, text="", font=("Arial", 14), fg="red")
label.pack()

window.mainloop()

#2
import tkinter as tk

def clear_text():
    entry.delete(0, tk.END)

def on_pressed(event):
    clear_text()

window = tk.Tk()
window.title("Очистка текстового поля")
window.geometry("400x400")

entry = tk.Entry(window, width=20, font=("Arial", 12), fg="black" )
entry.pack()

clear_button = tk.Button(window, text="Очистить", command=clear_text)
clear_button.pack()

window.bind("<Return>", on_pressed)

window.mainloop()
