# Exercise 1
# quantity = int(input("Enter the quantity: "))
# price = float(input("Enter the price: "))

# if quantity >=0 and price >= 0:
#     print("Data is valid")
# else:
#     print("Data is invalid")

# Exercise 2
# temperature = float(input("Enter the temperature: "))

# if temperature < 18:
#     print("Low temperature")
# elif temperature >= 18 and temperature <= 26:
#     print("Normal temperature")
# else:
#     print("High temperature")

# Exercise 3
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# if log['level'] == 'ERROR':
#     print(log['message'])

# Exercise 4
# age = int(input("Enter your age: "))
# email = input("Enter your email: ")

# if age < 18 and age <= 65:
#     print("User age is out of range")
# elif email.count('@') < 1 or email.count('.') == 0:
#     print("User email is invalid")
# else:
#     print("User data is valid")

# Exercise 5
# transaction = {'value': 12000, 'hour': 20}
# if transaction['value'] > 10000 and (transaction['hour'] < 9 or transaction['hour'] > 18):
#     print("Transaction suspicious")
# else:
#     print("Transaction is normal")

# Exercise 6

# text = "a raposa marrom salta sobre o cachorro preguiçoso"
# words = text.split()
# count_words = {}

# for word in words:
#     if word in count_words:
#         count_words[word] += 1
#     else:
#         count_words[word] = 1

# print(count_words)

# Exercise 7

numbers = [10,20, 30, 40, 50]
minimo = min(numbers)
maximo = max(numbers)
normalizados = [(x - minimo) / (maximo - minimo) for x in numbers]
print(normalizados)
