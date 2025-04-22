#Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем записать их произведение в файл output.txt.



with open('input.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))
product = 1
for num in numbers:
    product *= num
with open('output.txt', 'w') as f:
    f.write(str(product))