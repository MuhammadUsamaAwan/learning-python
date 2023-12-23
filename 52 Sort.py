students = ["spongbob", "patrick", "sandy", "squidward", "mr.krabs"]

students.sort()
print(students)

students.sort(reverse=True)
print(students)

students = ("spongbob", "patrick", "sandy", "squidward", "mr.krabs")
sorted_students = sorted(students)
print(sorted_students)

students = (
    ["spongbob", 400],
    ["patrick", 300],
    ["sandy", 500],
    ["squidward", 100],
    ["mr.krabs", 900],
)
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
