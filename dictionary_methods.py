student = {
    "name": "Harini",
    "age": 20,
    "course": "CSE",
    "city": "Hyderabad"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("name"))

student.update({"age": 21})
print("After Update:", student)

student.pop("city")
print("After Pop:", student)
