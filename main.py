# 1-3 пункт
name = "Екатерина"
print('Your name is', name)
age = "19"
print('Your name is', name, 'and you are', age)
print(name * 5)

user_name_str = input('What is your name? ')
# проверка ввода имени
if not user_name_str.isalpha():
    print('Name must contain only letters.'), exit(0)

print('Hello, ' + user_name_str)
user_age_str = input('How old are you? ')

# проверка ввода возраста
try:
    user_age_int = int(user_age_str)
except ValueError:
    print('You did not enter a number. Insert the number.')

if 30 >= user_age_int > 0:
    print('Your age is', user_age_int, '\nYou are so young')
elif 0 < user_age_int < 150:
    print('Your age is', user_age_int, '\nYou are so old')
elif user_age_int < 0:
    print('You entered a negative number.'), exit(0)
elif user_age_int > 150:
    print('You entered too big number.'), exit(0)

# обработка возраста
if user_age_int < 10:
    print("Sum of age digits:", user_age_int)
elif 10 <= user_age_int <= 99:
    sum_age = (user_age_int // 10) + (user_age_int % 10)
    print("Sum of age digits:", sum_age)
    mult_age = (user_age_int // 10) * (user_age_int % 10)
    print("Product of age digits:", mult_age)
elif 100 <= user_age_int <= 150:
    decade_num = (user_age_int // 10)
    mid_num = (decade_num % 10)
    sum_age = (user_age_int // 100) + mid_num + (user_age_int % 10)
    print("Sum of age digits:", sum_age)
    mult_age = (user_age_int // 100) * mid_num * (user_age_int % 10)
    print("Product of age digits:", mult_age)

# обработка имени
kol = len(user_name_str)
print("backwards:", user_name_str[::-1])
if kol >= 3:
    print("2-last but one symbols:", user_name_str[1:kol - 1])
    print("last 3 symbols:", user_name_str[kol - 3:kol])
if kol >= 5:
    print("first 5 symbols:", user_name_str[:5])
print("number of letters in the name:", kol)
print("Big letters:", user_name_str.upper())
print("Small letters:", user_name_str.lower())

# математическая задача
answer = input("2+2=? ")
if answer == "4":
    print("True")
else:
    print("False")
