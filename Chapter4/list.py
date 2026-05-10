friends = ["Apple", "banana", 5,43.3, "grape"]
print(friends[0]) 
friends[0]= "orange" # Unlink Strings are immutable but lists are mutable
print(friends[0])
friends.append("watermelon") # add new element to the end of the list
print(friends)
l1 = [1,2,3,5,4,7,6]
l1.sort() # sort the list in ascending order    
print(l1)
l1.reverse() # reverse the list
print(l1)
l1.insert(1, 0) # insert 0 at index 1
print(l1)   
l1.pop(1) # remove the element at index 1
print(l1)