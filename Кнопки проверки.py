#1
import tkinter as tk

def update_label():
    selected_options = [option for option, var in checkbox_vars.items() if var.get() == 1]
    result_label.config(text=f"Выбранные опции: {', '.join(selected_options)}")

root = tk.Tk()
root.title("Простой интерфейс с кнопками проверки")

checkbox_vars = {}

options = ["Кнопка №1", "Кнопка №2", "Кнопка №3"]

for option in options:
    var = tk.IntVar()
    checkbox_vars[option] = var
    checkbox = tk.Checkbutton(root, text=option, variable=var)
    checkbox.pack(anchor="w")

update_button = tk.Button(root, text="Показать", command=update_label)
update_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()

#2 & 3
import tkinter as tk

def show_results():
    selected_answers = []
    correct_answers = []

    for question, options in quiz.items():
        selected_answer = selected_vars[question].get()
        selected_answers.append((question, options[selected_answer]))
        correct_answers.append((question, options[0]))

    correct_label.config(text="Правильные ответы:\n" + "\n".join(f"{question}: {answer}" for question, answer in correct_answers))

root = tk.Tk()
root.title("Тест")

quiz = {
    "Столица Франции?": ["Париж", "Рим", "Ницца"],
    "Кто написал 'Ромео и Джульета'?": ["У. Шекспир", "Вольтер", "Жан-Жак Руссо"],
    "Создатель аналитической геометрии?": ["Р. Декарт", "Г. Галилей", "И. Ньютон"]
}

selected_vars = {}

for question, options in quiz.items():
    selected_vars[question] = tk.IntVar()
    tk.Label(root, text=question).pack()

    for i, option in enumerate(options):
        tk.Radiobutton(root, text=option, variable=selected_vars[question], value=i).pack(anchor="w")

    tk.Label(root, text="").pack()

show_button = tk.Button(root, text="Показать результаты", command=show_results)
show_button.pack(pady=10)

correct_label = tk.Label(root, text="")
correct_label.pack()

root.mainloop()
