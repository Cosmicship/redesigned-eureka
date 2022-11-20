ticket_price = [0,990,1390]
price = 0
try:
    tickets = int(input("Введите количество билетов: ")) #Количество билетов
except ValueError as error:
    print("Вы указали некорректное количество")
else:
    for i in range(tickets):
        age = int(input(f"Укажите возраст посетителя {i+1}: "))
        if age in range(18,26):
            price += ticket_price[1]
        elif age in range(26,100):
            price += ticket_price[2]
        else:
            price += ticket_price[0]
    if tickets > 3:
        print(f"Стоимость ваших билетов с учетом скидки 10% составляет {round(price*0.9)} руб.")
    else:
        print(f"Стоимость ваших билетов составляет {price} руб.")
