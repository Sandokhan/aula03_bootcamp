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
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])