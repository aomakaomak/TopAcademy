user_name = input("Введите свои имя и фамилию: ")
recipient_name = input("Введите имя и фамилию адресата: ")
message = input("Введите сообщение: ")

greeting = f"Уважаемый {recipient_name}!"
bye = f"С уважением, {user_name}"
print(greeting.center(40))
print(message.ljust(40))
print(bye.rjust(40))
