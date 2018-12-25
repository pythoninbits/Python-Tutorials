# Tutorial to print variables in python
# reference https://www.python-course.eu/python3_formatted_output.php

# Declare a variable and initialize it

int_type = 1046565
float_type = 1.234587912
string_type1 = "Python"
string_type2 = "In"
string_type3 = "Bits"

x = 10
y = 20

# print integer variable
print("a = ",int_type)

# print float variable
print("b = ",float_type)

# print variables with precision
print("a = %5d \nb = %3.2f"%(int_type,float_type))

# print string variables - using spe 
print(string_type1 , string_type2 , string_type3, sep = " ")

# print string variables - concating strings
print("Hello" + "   " + "World")

# print using format method
print("{0} * {1} = {2}".format(x,y,x*y))
