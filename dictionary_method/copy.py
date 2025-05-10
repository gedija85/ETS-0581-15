student = {"name": "Abebe", "age": 20}
new_student = student.copy()
new_student["age"] = 21
print(student)             # {'name': 'Abebe', 'age': 20}
print(new_student)         # {'name': 'Abebe', 'age': 21}
