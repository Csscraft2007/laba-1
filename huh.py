def count_jewels_in_stones(J, S):
   """
    jewels = set(J)  # Создаем множество для быстрой проверки
    count = 0
    for stone in S:
        if stone in jewels:
            count += 1
    return count
J = "ab"
S = "aabbccd"
result = count_jewels_in_stones(J, S)
print(result)
