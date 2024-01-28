#1
import csv

def filters_csv(csv_file_path):
    with open (csv_file_path,"r", newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Name'].startswith('A'):
                print(row)

csv_file_path = 'data.csv'

filters_csv(csv_file_path)

#2
import csv

def read_books(csv_file_path):
    with open(csv_file_path, "r", newline='') as file:
        csv_reader = csv.DictReader(file)
        books = [row for row in csv_reader]
    return books

def add_book(books, new_book):
    books.append(new_book)

def write_books(csv_file_path, books):
    with open(csv_file_path, "w", newline='') as file:
        fieldnames = ['Название', 'Автор', 'Год издания']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        csv_writer.writeheader()
        csv_writer.writerows(books)

csv_file_path = 'librar.csv'
existing_books = read_books(csv_file_path)

new_book = {'Название': 'Время моей жизни', 'Автор': 'Сесилия Ахерн', 'Год издания': '2011'}
add_book(existing_books, new_book)

write_books(csv_file_path, existing_books)

print("Книга успешно добавлена и файл обновлен.")

