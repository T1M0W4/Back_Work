from functools import reduce
students = (
            {'name': 'Alex Novak', 'age': 21, 'course': 'Python', 'average_grade': 9.78},
            {'name': 'Peter Sullivan', 'age': 21, 'course': 'Python', 'average_grade': 9.00},
            {'name': 'Akane Tendo', 'age': 19, 'course': 'HTML', 'average_grade': 4.72},
            {'name': 'Hidetaka Miyadzaki', 'age': 23, 'course': 'Python', 'average_grade': 12.00},
            {'name': 'Ken Levin', 'age': 21, 'course': 'HTML', 'average_grade': 8.98},
            {'name': 'Kaya Scodelario', 'age': 20, 'course': 'Python', 'average_grade': 11.89},
            {'name': 'Nat King', 'age': 23, 'course': 'Python', 'average_grade': 6.25},
            {'name': 'Leya Argano', 'age': 23, 'course': 'Python', 'average_grade': 11.25}
            )

python_students = tuple(filter(lambda x: x['course'] == 'Python', students))
print(tuple(python_students))


sum_grades = reduce(lambda acc, x: acc+x['average_grade'], python_students, 0)
mean_grades = sum_grades/len(python_students)

sum_ages = reduce(lambda acc, x: acc+x['age'], students, 0)
mean_ages = sum_ages/len(students)

print(f'Mean grade: {mean_grades}\nMean age: {mean_ages}')