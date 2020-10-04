"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32

print(64 + 32)

# 2.- Do the same as the question one but this time use variables instead of # numbers.

a = 64
b = 32
print(a + b)

# another solution
x = 64 + 32
print(x)

# 3.- Make a program that prints a sentence that includes at least 3 variables.

y = "May"
w = "force"
z = "you"
Yoda = y + " the " + w + " be with " + z
print(Yoda)

# 4.- Given a sentence, assign the string to a variable then print the number of characters in the sentence. 
# The sentence is "This is my first Python program."

sentence = "This is my first Phyton program."
print(len(sentence))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as follows: The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>

# There's a few ways of doing this code, e.g.
# With Float numbers
value_1 = 1920 * 0.10 + 1920
value_2 = 1080 * 0.10 + 1080
print("The 10% overscan of 1920 is " + str(value_1) + ", and the 1080 is " + str(value_2))

# With Integers numbers
value_3 = 1920 * 10 / 100 + 1920
value_4 = 1080 * 10 / 100 + 1080
print("The 10% overscan of 1920 is " + str(value_3) + ", and the 1080 is " + str(value_4))