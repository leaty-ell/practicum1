#10
flight_number = input("Введите номер рейса: ")
airline_name_rus = input("Введите название авиакомпании (на русском языке): ")
airline_name_eng = input("Введите название авиакомпании (на английском языке): ")
arrival_city_rus = input("Введите город прилета (на русском языке): ")
arrival_city_eng = input("Введите город прилета (на английском языке): ")

announce_rus = f"Заканчивается посадка на рейс {flight_number} {airline_name_rus} до {arrival_city_rus}"
announce_eng = f"This is the final boarding call for {airline_name_eng} flight {flight_number} to {arrival_city_eng}"

print(announce_rus)
print(announce_eng)