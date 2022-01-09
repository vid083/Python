# create an empty dict
empty_dict = {}

# add neww items to dictionary
empty_dict["vidya"] = 123
empty_dict["vivek"] = "Hello"
print(empty_dict)

# wipe an existing dictionary
# empty_dict = {}
print(empty_dict)

# edit an item in a dictionary 
empty_dict["vivek"] = "Hello yaar"
print(empty_dict)

# loop through a dictionary
for key in empty_dict:
    print(key)
    print(empty_dict[key])