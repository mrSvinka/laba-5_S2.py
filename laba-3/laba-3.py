#В текстовом файле записаны сведения о детях из детского сада в следующей форме (создать не менее 5 записей, с разным возрастом):
#Фамилия пробел Имя пробел возраст
#Иванов Иван 5
#Необходимо записать в отдельные текстовые файлы самого старшего и самого младшего


mini = float('inf')
maxi = -float('inf')
all = []

with open('children.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        surname, name, age = line.rsplit(' ', 2)  # Разбиваем строку на 3 части
        age = int(age)
        all.append((age, line))

        if age < mini:
            mini = age
        if age > maxi:
            maxi = age

with open('youngest.txt', 'w', encoding='utf-8') as f:
    for age, child in all:
        if age == mini:
            f.write(child + '\n')

with open('oldest.txt', 'w', encoding='utf-8') as f:
    for age, child in all:
        if age == maxi:
            f.write(child + '\n')