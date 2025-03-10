import random

def get_numbers_ticket(min: int, max: int, quantity: int)-> list[int]:
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
        
        if quantity > (max + min):
            return "Помилка: Кількість чисел більше, ніж доступний діапазон"
        elif min >=1 < max <=1000:
            result = random.sample(range(min, max +1), quantity)
            return result  
        else:
            return "Помилка: Введіть числa від 1 до 1000"
    except ValueError:
        return "Помилка: Введіть числові значення"   

print(get_numbers_ticket(1, 40, 6))