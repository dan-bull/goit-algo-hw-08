import heapq

def minimize_connection_cost(cables):
    # Перетворюємо список кабелів у мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягаємо два найменших елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислюємо витрати на їх об'єднання
        combined_length = first + second
        total_cost += combined_length
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, combined_length)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на об'єднання кабелів: {minimize_connection_cost(cables)}")
