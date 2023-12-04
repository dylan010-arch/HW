import tkinter as tk

def on_button_click():
    user_input = entry.get()
    label_result.config(text=f"Привет, {user_input}!")

root = tk.Tk()
root.title("Добро пожаловать")
root.geometry("450x450")

label = tk.Label(root, text="Введите ваше имя:" , font=("Arial", 10), fg="black")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Привет!", command=on_button_click,  font=("Arial", 10), fg="black")
button.pack()

label_result = tk.Label(root, text="",  font=("Arial", 14), fg="black")
label_result.pack()

root.mainloop()
