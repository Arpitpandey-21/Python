a = (1, 2, 3, 4, 5)
print(type(a))
b = (1,)
print(type(b))
#tuple is immutable, we cannot change the value of a tuple after it is created
# a[0] = 10 # This will raise an error
# We can concatenate two tuples
c = a + b
print(c)
# We can also repeat a tuple
d = a * 2
print(d)
# We can also unpack a tuple
e = (1, 2, 3)
x, y, z = e
print(x, y, z)
print(a.count(1)) # count the number of times 1 appears in the tuple