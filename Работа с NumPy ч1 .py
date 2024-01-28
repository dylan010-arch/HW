#1
import numpy as np

def sum_rows (arr):
    row_sum = np.sum(arr, axis=1)
    return row_sum

arr1 = np.random.randint (1,10, size=(3,3))
arr2 = np.random.randint (1,10, size=(3,3))

result = np.multiply (arr1, arr2)
print (f"Array 1:{arr1}")
print (f"Array 2:{arr2}")

sums_row1 = sum_rows(arr1)
sums_row2 = sum_rows(arr2)
print (f"Summa 1{sums_row1}")
print (f"Summa 2{sums_row2}")

#2
import numpy as np

data = np.random.rand(100)

mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)

print("Среднее значение:", mean_value)
print("Медиана:", median_value)
print("Стандартное отклонение:", std_deviation)
