#1
import pandas as pd

data = {
    'Имя': ['Анара', 'Иван', 'Мария', 'Азамат'],
    'Возраст': [21, 22, 21, 22],
    'Пол': ['Женский', 'Мужской', 'Женский', 'Мужской'],
    'GPA': [3.62, 3.53, 3.2, 3.8]
}

students_df = pd.DataFrame(data)

print(students_df)

#2
print("Столбец 'Имя' для всех студентов:")
print(students_df['Имя'])

female_students = students_df[students_df['Пол'] == 'Женский']
print("\nСтуденты женского пола:")
print(female_students)

max_gpa_student = students_df.loc[students_df['GPA'].idxmax()]
print("\nСтудент с наивысшим баллом GPA:")
print(max_gpa_student)

#3
students_df['Возраст'] = students_df['Возраст'] + 1

print("Обновленный DataFrame с увеличенным возрастом:")
print(students_df)

youngest_student = students_df.loc[students_df['Возраст'].idxmin()]

students_df.at[youngest_student.name, 'GPA'] += 0.5

print("\nОбновленный DataFrame с обновленным баллом GPA:")
print(students_df)

#4
new_student_data = {'Имя': 'Толагай', 'Возраст': 22, 'Пол': 'Мужской', 'GPA': 3.69}
students_df = students_df.append(new_student_data, ignore_index=True)

print("Обновленный DataFrame с новым студентом:")
print(students_df)

#5
students_df['GPA'] = students_df['GPA'].apply(lambda x: x + 0.5)

print("Обновленный DataFrame с увеличенным GPA:")
print(students_df)

#6
sorted_by_age_desc = students_df.sort_values(by='Возраст', ascending=False)

print("Студенты, отсортированные по возрасту по убыванию:")
print(sorted_by_age_desc)

sorted_by_gpa_asc = students_df.sort_values(by='GPA', ascending=True)
print("\nСтуденты, отсортированные по GPA по возрастанию:")
print(sorted_by_gpa_asc)

#7
students_df.to_csv('student.csv', index=False)
print("DataFrame сохранен в файл 'student.csv'")






