lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for num in lst:
    if num < 30 and num % 3 == 0:
        print(num)
result = [num for num in lst if num < 30 and num % 3 == 0]
print("\n Результат в виде списка:", result)

