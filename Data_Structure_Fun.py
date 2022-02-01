#2D lists (grid-like)
#3D lists (cube-like)
#there are two ways to look at 2d lists
#1st as a table 
matrix = [  [1,2,3],
            [4,5,6],
            [7,8,9]]
print(matrix[1][2])

#3D lists
cube = [[[0,0],[1,1]],[[2,2],[3,3]]]
print(cube[0][0][0])

#Tuple is a immutable list
my_tuple = "x", "y", "z" #automatic parentheses
print(my_tuple)
print(type(my_tuple))

#in order to create a one item tuple you have to use a comma so its not interpreted as an operator
my_single_tuple = (1, )
print(my_single_tuple)
#to create an empty tuple 
my_empty_tuple = tuple()
print(my_empty_tuple)

#DICTIONARIES
#list with keys as indexes and values mapped from those keys
# a key value pair is where a value is used to look up another value
#keys in a dictionary MUST be unique
#example: key is student id where as the value is the student name
my_dict = {}
my_dict["12345"] = "Jane Doe"
print(my_dict)
state_capitals  = {"Washington": "olympia"}
state_capitals["Washington"] = "spokane"
print(state_capitals)
state_capitals["california"] = "Sacremento"
print(state_capitals)
# the key value pairs in a dictionary are not ordered
roman_numerals = dict([("I", 1),("V", 5), ("X",10), ("L",50)])
print(roman_numerals)
roman_numerals_as_list = list(roman_numerals.items())
print(roman_numerals_as_list)

#types for keys can be integers, stings, tuples, files, etc.
#However a list CAN NOT be used as a key in a dictionary

#len() also works with tuples and dictionaries
print(len(state_capitals))
print("Washington" in state_capitals)  #testing for keys in dictionary
print("spokane" in state_capitals)     #spokane is not a key but is a value in the dictionary

#loop through the key pairs in a dictionary
for state in state_capitals:
    print(state, state_capitals[state])
for (state, capital) in state_capitals.items():
    print(state, "*", capital)