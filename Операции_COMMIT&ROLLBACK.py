#1
import sqlite3

conn = sqlite3.connect('db_27.db')
cursor = conn.cursor()
conn.execute('BEGIN;')

update_salary_query = "UPDATE employees SET salary = salary * 1.05;"
cursor.execute(update_salary_query)

update_price_query = "UPDATE products SET price = price * 1.1 WHERE stock_quantity > 10;"
cursor.execute(update_price_query)
conn.commit()
print("Transaction committed successfully.")

conn.close()

#2
import sqlite3

conn = sqlite3.connect('db_27.db')
cursor = conn.cursor()
conn.execute('BEGIN;')

update_salary_query = "UPDATE employees SET salary = salary * 1.05;"
cursor.execute(update_salary_query)
conn.execute('SAVEPOINT my_savepoint;')

update_price_query = "UPDATE products SET price = price * 1.1 WHERE stock_quantity > 10;"
cursor.execute(update_price_query)

conn.execute('RELEASE my_savepoint;')
print("Savepoint changes committed successfully.")
conn.commit()
print("Transaction committed successfully.")

conn.close()

#3
import sqlite3

try:
    conn = sqlite3.connect('db_27.db')
    cursor = conn.cursor()

    conn.execute('BEGIN;')
    update_salary_query = "UPDATE employees SET salary = salary * 1.05;"
    cursor.execute(update_salary_query)
    conn.execute('SAVEPOINT my_savepoint;')

    try:
        update_price_query = "UPDATE products SET price = price * 1.1 WHERE stock_quantity > 10;"
        cursor.execute(update_price_query)
        raise sqlite3.Error("Simulated error after savepoint")

    except sqlite3.Error as savepoint_error:
        conn.execute('ROLLBACK TO my_savepoint;')
        print("Changes rolled back to the savepoint.")

    conn.commit()
    print("Transaction committed successfully.")

finally:
    conn.close()

