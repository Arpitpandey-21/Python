d = {} # Empty dictionary
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
#print(marks, type(marks))
print(marks.values())
print(marks.keys())

marks.update({"Alice":99,"arpit":100})
print(marks)
print(marks.get("alice2")) # prints none
#print(marks["Alice2"])  #returns a error