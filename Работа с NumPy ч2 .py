import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([2, 4, 6])

result1 = array1 * array2
print("Поэлементное умножение:")
print(result1)

result2 = array1 ** array2
print("\n Возведение в степень:")
print(result2)

scalar = 2
result3_array1 = array1 / scalar
result3_array2 = array2 / scalar
print("\n Деление на скаляр:")
print("array1 / scalar:")
print(result3_array1)
print("array2 / scalar:")
print(result3_array2)


additional_array = np.array([1, 1, 1])
result4 = (array1 * array2) + additional_array
print("\n Пример Broadcasting с умножением и сложением:")
print(result4)
