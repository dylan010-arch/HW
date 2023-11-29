#1
import tkinter as tk

def exit():
    window.destroy()
window = tk.Tk()
window.title(" Tkinter")
window.geometry("450x450")

label = tk.Label(window, text="Привет! \n Нажми на кнопку Выход")
label.pack(pady=20)

exit_button = tk.Button(window, text="Выход", command=exit)
exit_button.pack(pady=20)

window.mainloop()

#2
import tkinter as tk

def profile():
    window = tk.Tk()
    window.title("Анкета обо мне")
    window.geometry("450x450")

    label = tk.Label(window, text="Имя: Толагай\nВозраст: 22\nГород: Астана\nХобби: Воллейбол, Видеомейкинг")
    label.pack(padx=20, pady=20)

    window.mainloop()
    
profile()
