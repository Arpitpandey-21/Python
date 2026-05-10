a = 13
t = type(a) # type() is a built-in function that returns the type of an object. In this case, it will return <class  'int'>, indicating that 'a' is an integer.
print(t) 

b = 3.14
t = type(b) # This will return <class 'float'>, indicating that 'b' is a floating-point number. 
print(t)
s = "Hello, World!"
t = type(s) # This will return <class 'str'>, indicating that 's' is a string.  
print(t)    
# "3.14" is a string representation of the number 3.14, and it is not the same as the float value 3.14.
t = type("3.14") # This will return <class 'str'>, indicating that "3.14" is a string, not a float.
print(t)    

x = "3.144"
t = type(x) # This will return <class 'str'>, indicating that 'x' is a string, even though it looks like a number.
y = float(x)
print(t)
print(type(y)) # This will return <class 'float'>, indicating that 'y' is a floating-point number after conversion from the string 'x'. 