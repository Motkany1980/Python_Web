print("Start")
##Get back the first character of the string
# print( "Hello World"[0])
# ## Data types

# print(type(42))  # Output: <class 'int'>
# print(type(3.14))  # Output: <class 'float'>
# print(type("hello"))  # Output: <class 'str'>
# print(type(True))  # Output: <class 'bool'>
# print(type([1, 2, 3]))  # Output: <class 'list'>
# print(type((1, 2, 3)))  # Output: <class 'tuple'>
# print(type({'name': 'John', 'age': 25}))  # Output: <class 'dict'>
# print(type({1, 2, 3}))  # Output: <class 'set'>

# num_char=len(input("What is your name..."))
# print(type(num_char))
# print("Your name has "+str(num_char)+" characters")

# a=float (123)
# print(type(a))


# two_digit_number = input("Type a two digit number: ")
# if not two_digit_number.isdigit() or len(two_digit_number) != 2:
#     print("Please enter a number")
# else: 
#     print(str(two_digit_number[0])+" - "+str(two_digit_number[1]))
    
# days=round(((365*90)-(365*43))/7)
# print(f"I hve {days} weeks left")

print("Welcome to the tip calculator")
totalBill=int(input("What is the total bill?"))
tip=input("What percentage tip would you like to give? 10, 12 or 15?")
people=int(input("How many people to split the bill?"))
tipAmount=(totalBill*int(tip))/100      
totalAmount=totalBill+tipAmount
eachPerson=totalAmount/people
print(f"The total cost is {totalAmount}'with the tipps', \n Each person should pay {eachPerson} ")