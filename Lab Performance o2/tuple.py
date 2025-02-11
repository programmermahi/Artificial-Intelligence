students = (
    ("Alice", 20, 85),
    ("Bob", 22, 90),
    ("Charlie", 21, 78),
    ("David", 23, 92),
    ("Eve", 19, 88)
)
sorted_students = sorted(students, key=lambda x: x[2])

print(sorted_students)
