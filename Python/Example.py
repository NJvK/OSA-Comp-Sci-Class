import math

print (4 + 5)

students = ["Yara", "Lucas", "Nia"]

students.append("Faisal")

print(students [2])
print(students [-2])

value = students.pop()
print(value)
print(students)

if "Faisal" in students:
    print("Faisal is in the list")
else: 
    print("Faisal is not in the list")

for student in students:
    print(student + " studies CS")

atlas = {"Georgia": "Tbilisi", "Armenia": "Yerevan", "Azerbaijan": "Baku"}

atlas["Turkey"] = "Ankara"

print(atlas["Georgia"])

for country in atlas:
    print(country + " has the capital of " + atlas[country])

while True:
    message = float(input ("Type a big number: "))
    if (message > 1000):
        print("The number is odd")
    else:
        break


