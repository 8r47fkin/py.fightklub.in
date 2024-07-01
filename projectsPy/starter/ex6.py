# assigned a variable
types_of_people = 10
# assigned variable with a function calling a variable previously assigned
x = f"there are {types_of_people} types of people."

# assigned a variable
binary = "binary"

# assigned a variable
do_not = "don't"

# assigned a variable with calling a variable previously assigned
y = f"those who know {binary} and those who {do_not}."

# printing a variable which has a variable inside a variable
print(x)
print(y)

# printing variable inside a variable with a variable
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assigned a boolean, then a variable, then checked it with boolean
hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"
print(joke_evaluation.format(hilarious))

# concatenate a variable

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)