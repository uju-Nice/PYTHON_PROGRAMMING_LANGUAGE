
# #!/usr/bin/env python3  

# # 1. comments
# # This is a single-line comment
# # This is a multi-line comment(using triple quotes ex: '''This is a multi-line comment''')
# # print("This code will run")  # This is an inline comment


# # 2. variables & data types (integer, float, string, boolean)
a = 10 
#  type(a)  # Output: <class 'int'>
b = 20.5  
# type(b)  # Output: <class 'float'>    
c = "Hello python!" 
# type(c)  # Output: <class 'str'>
d = True    
# type(d)  # Output: <class 'bool'>
sum = a + b    
print(a + b)    
print(sum)  

# # 3. indentation & functions(using spaces or tabs to define code blocks)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# #  4. operators(arithmetic, comparison, logical, assignment, bitwise)
a = 20
b = 10  
# # arithmetic operations
print(a + b)  # Output: 30  
print(a - b)  # Output: 10
print(a * b)  # Output: 200
print(a / b)  # Output: 2.0
# # comparison operations
print(a > b)  # Output: True
print(a < b)  # Output: False
print(a == b)  # Output: False  
# print(a != b)  # Output: True 

# # logical operations
print(a > 15 and b < 15)  # Output: True
print(a > 15 or b < 5)    # Output: True
print(not(a > 15))  # Output: False
print(not(b < 15))  # Output: False

# # bitwise operations
# # a = 5  # In binary: 0101
# # b = 3  # In binary: 0011
# # print(a & b)  # Output: 1 (In binary: 0001)
# # print(a | b)  # Output: 7 (In binary: 0111)
# # print(a ^ b)  # Output: 6 (In binary: 0110)
# # print(~a)     # Output: -6 (In binary: 1010)

# # assignment operations
a = 10
a += 5  # Equivalent to a = a + 5
print(a)  # Output: 15
a -= 3  # Equivalent to a = a - 3
print(a)  # Output: 12
a *= 2  # Equivalent to a = a * 2
print(a)  # Output: 24
a /= 4  # Equivalent to a = a / 4
print(a)  # Output: 6.0   

# # 5. data structures(list, tuple, dictionary, set)
# # list
# # l_list = [1, 2, 3, 4, 5]
# # print(l_list)
# # print(l_list[1])  # Output: 1

# # tuple
# # t_tuple = (1, 2, 3, 4, 5)
# # print(t_tuple)  # Output: (1, 2, 3, 4, 5)
# # print(t_tuple[0])  # Output: 1

# # dictionary
# # d_dict = {"name": "Nice", "age": 30}
# # print(d_dict) 
# # print(d_dict["name"])  # Output: Nice

# # set
# # s_set = {1, 2, 3, 4, 5}
# # print(s_set)  # Output: {1, 2, 3, 4, 5}

# # 7. input_output  (input and print)
# # name = input("Enter your name: ")
# # print(f"Hello, {name}!")
# # age = input("Enter your age: ")
# # print(f"You are {age} years old.")
# # country = input("Enter your country: ")
# # print(f"You are from {country}.")

# # 8. classes and_objects(defining classes and creating objects)
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def greet(self):
# #         return f"Hello, my name is {self.name} and I am {self.age} years old."

# # person1 = Person("Alice", 30)
# # print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

# # 9. exception_handling(try, except, finally, raise, assert, with, as,)
# # try:
# #     result = 10 / 2
# # except ZeroDivisionError:
# #     print("Cannot divide by zero!")

# # 10.file_handling (open, read, write)
# # with open("tutorials.txt", "w") as file:
# #     file.write("Hello, World!")

# # with open("tutorials.txt", "r") as file:
# #     content = file.read()
# #     print(content)  # Output: Hello, World!

# # 11.modules_and_packages_package mamanger( importing and using modules and packages, pip)
# # import math 
# # print(math.sqrt(25))  


# # 12. functions(defining and calling functions)
# # def add(x, y):
# #     return x + y
# # print(add(10, 20))

# # 13. loop (for, while)
# # l = [10, 20, 30, 40, 50]
# # for item in l:
# #     print(item)

# # for i in range(5):    
# #     print(i)

# # i = 1
# # while(i < 5):
# #     print(i)    
# #     i += 1


# 14. conditional_statements (if, elif, else)
# x = 3
# if x > 5:
#     print("x is greater than 5")
# elif x > 0:
#     print("x is greater than 0 ")
# else:
#     print("x is less than 0")

# 15. python script(creating and running a python script)








