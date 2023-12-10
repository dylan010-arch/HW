import tkinter as tk
from tkinter import ttk

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore")

        frame_combobox = tk.Frame(root)
        frame_combobox.pack(pady=10)

        self.books = ["Властелин Колец", "Великий Гэтсби", "Северный Полюс", "Гарри Поттер", "Игра престолов"]
        self.selected_book = tk.StringVar()
        self.book_combobox = ttk.Combobox(frame_combobox, values=self.books, textvariable=self.selected_book)
        self.book_combobox.grid(row=0, column=0, padx=10)

        frame_price = tk.Frame(root)
        frame_price.pack(pady=10)

        self.display_price_label = tk.Label(frame_price, text="Стоимость:")
        self.display_price_label.grid(row=0, column=0, padx=10)

        find_button = tk.Button(frame_price, text="Узнать стоимость", command=self.display_price)
        find_button.grid(row=0, column=1, padx=10)

        self.prices = {"Властелин Колец": 4500, "Великий Гэтсби": 3150, "Северный Полюс": 2000, "Гарри Поттер": 2500, "Игра престолов": 4300}
        self.display_price()

    def display_price(self):
        selected_book = self.selected_book.get()
        if selected_book in self.prices:
            price = self.prices[selected_book]
            self.display_price_label.config(text=f"Стоимость: {price} Т")
        else:
            self.display_price_label.config(text="Выберите книгу")

root = tk.Tk()
app = BookstoreApp(root)
root.mainloop()
