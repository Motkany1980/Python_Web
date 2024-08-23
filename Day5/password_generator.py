import datas
import random


print("Welcome to the PyPassword Generator! \n How many letters would you like in your password?")

nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))

password=""

for letter in range(1,nr_letters+1):
    password+=random.choice(datas.letters)  
for symbol in range(1,nr_symbols+1):
    password+=random.choice(datas.symbols)
for number in range(1,nr_numbers+1):
    password+=random.choice(datas.numbers)
    
print(password)