student = {"name": "Abebe", "age": 20}
student.get("name")           # 'Abebe'
student.get("grade")          # None
student.get("grade", "N/A")   # 'N/A'
student.get("age")