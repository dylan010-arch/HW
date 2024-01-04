import sqlite3

conn = sqlite3.connect('db_27.db')
cursor = conn.cursor()

# 1.
query1 = 'SELECT * FROM orders;'
cursor.execute(query1)
result1 = cursor.fetchall()
print("Query 1 result:")
if result1:
    for row in result1:
        print(row)
print()

# 2.
query2 = 'SELECT DISTINCT category FROM products;'
cursor.execute(query2)
result2 = cursor.fetchall()
print("Query 2 result:")
if result2:
    for row in result2:
        print(row)
print()

# 3.
query3 = 'SELECT customer_name FROM customers WHERE balance > 1000.00;'
cursor.execute(query3)
result3 = cursor.fetchall()
print("Query 3 result:")
if result3:
    for row in result3:
        print(row)
print()

# 4.
query4 = 'SELECT * FROM employees ORDER BY salary DESC;'
cursor.execute(query4)
result4 = cursor.fetchall()
print("Query 4 result:")
if result4:
    for row in result4:
        print(row)
print()

# 5.
query5 = 'UPDATE employees SET salary = salary * 1.05;'
cursor.execute(query5)
conn.commit()
print("Query 5: Salary updated.")
print()

# 6.
query6 = "UPDATE orders SET status = 'Processing' WHERE delivery_country = 'USA';"
cursor.execute(query6)
conn.commit()
print("Query 6: Orders status updated.")
print()

# 7.
query7 = "UPDATE products SET price = price * 0.9 WHERE stock_quantity < 20;"
cursor.execute(query7)
conn.commit()
print("Query 7: Product prices updated.")
print()

# 8.
query8 = "UPDATE customers SET status = 'Active' WHERE balance > 5000;"
cursor.execute(query8)
conn.commit()
print("Query 8: Customer status updated.")
print()

conn.close()
