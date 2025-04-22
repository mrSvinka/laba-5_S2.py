#Дан файл в котором записаны в столбик (каждое на отдельной строке) целые числа, всего 10 чисел. Отсортировать их по возрастанию цифр и записать в другой файл.



with open('input2.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f.readlines()]
numbers.sort()
with open('output2.txt', 'w') as f:
    f.write('\n'.join(map(str, numbers)))