#В текстовом файле записаны сведения о детях из детского сада в следующей форме (создать не менее 5 записей, с разным возрастом):
#Фамилия пробел Имя пробел возраст
#Иванов Иван 5
#Необходимо записать в отдельные текстовые файлы самого старшего и самого младшего



# Читаем данные из файла и обрабатываем
min_age = float('inf')
max_age = -float('inf')
all_children = []

with open('children.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        surname, name, age = line.rsplit(' ', 2)  # Разбиваем строку на 3 части
        age = int(age)
        all_children.append((age, line))

        # Обновляем минимальный и максимальный возраст
        if age < min_age:
            min_age = age
        if age > max_age:
            max_age = age

# Записываем результаты в отдельные файлы
with open('youngest.txt', 'w', encoding='utf-8') as f:
    for age, child in all_children:
        if age == min_age:
            f.write(child + '\n')

with open('oldest.txt', 'w', encoding='utf-8') as f:
    for age, child in all_children:
        if age == max_age:
            f.write(child + '\n')