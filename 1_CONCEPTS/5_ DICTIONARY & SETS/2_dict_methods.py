marks = {
    "Akash": 100,
    "Shruti": 97,
    "Shubham": 56,
    "Rohan": 23,
    1: "Akash"
}

print(marks.items())
print(marks)

print(marks.keys())
print(marks)

print(marks.values())
print(marks)

marks.update({"Akash": 99, "Renuka": 100})
print(marks)

print(marks.get("Akash2")) # Prints None
# print(marks["Akash2"]) # Returns an error