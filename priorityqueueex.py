''' append elements(key,value),
key= priority
value= element in queue
and sort the list everytime an element
is appended'''

students_grade= []
students_grade.append(1,"Andrew")
students_grade.append(4, "John")

students_grade.sort(reverse= True)
print("yes")
print(students_grade)

students_grade.append(3, "Jean")
students_grade.sort(reverse= True)

students_grade.append(2, "Matt")

students_grade.sort(reverse= True)
print("priority wise sorted")
print(students_grade)
print("Original queue")
while students_grade:
    print(students_grade.pop())
