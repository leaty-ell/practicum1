#12
def calculate_cost(total_cost, silver_watch_price, silver_watches_sold, gold_to_silver_ratio):
    gold_watches_sold = silver_watches_sold / gold_to_silver_ratio
    total_silver_cost = silver_watches_sold * silver_watch_price
    total_gold_cost = total_cost - total_silver_cost
    gold_watch_price = total_gold_cost / gold_watches_sold
    return gold_watch_price

total_cost = float(input("Введите общую стоимость часов: "))
silver_watch_price = 48
silver_watches_sold = 96
gold_to_silver_ratio = 16

gold_watch_price = calculate_cost(total_cost, silver_watch_price, silver_watches_sold, gold_to_silver_ratio)
print(f"Стоимость золотых часов: {gold_watch_price} руб.")