# Tutorial to print variables in python
# reference https://www.python-course.eu/python3_formatted_output.php


int_type1 = 123
int_type2= 777

# print integer variable
print(int_type)

print("Sample Value = ", int_type1)

# print 2 integer variables
print("Sample Value 1 = %d \nSample Value 2 = %d"%(int_type1,int_type2))

float_type = 45.23698456

# print float variable
print("float type value =",float_type)

# print variables with precision
print("float type value = %.2f"%(float_type))

string1 = "Hello"
string2 = "World"

# print string variables - concating strings
print(string1+string2)

# print string variables - using sep 
print(string1,string2, sep = " ")

# print string variables - using sep 
print(string1,string2,"Python",sep = " ")

for x in range(10):
    print(x)


y = 10

for x in range(10):
    # print using format method
    print("{0} * {1} = {2}".format(x,y,x*y))
