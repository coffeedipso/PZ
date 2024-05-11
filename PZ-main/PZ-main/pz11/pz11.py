with open('file1.txt', 'w', encoding='utf-8') as file1:
    file1.write("1 2 3 4 5 6")

with open('file2.txt', 'w', encoding='utf-8') as file2:
    file2.write("-1 -2 -3 -4 -5 -6")

with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('new_file.txt', 'w') as new_file:
    data1 = file1.read().split()
    data2 = file2.read().split()

    new_file.write(f"Элементы первого файла: {data1}\n")
    new_file.write(f"Элементы второго файла: {data2}\n")
    new_file.write(f"Количество элементов первого файла: {len(data1)}\n")
    new_file.write(f"Количество элементов второго файла: {len(data2)}\n")
    new_file.write(f"Сортировка элементов первого файла: {sorted(data1)}\n")
    new_file.write(f"Сортировка элементов второго файла: {sorted(data2)}\n")
    new_file.write(f"Элементы кратные 3 во втором файле: {[x for x in data2 if int(x) % 3 == 0]}\n")

with open('text18-33.txt', 'r', encoding='utf-8') as original_file:
    content = original_file.read()
    space_count = content.count(' ')
    print("Содержимое файла text18-33.txt:")
    print(content)

    user_phrase = input("Введите фразу для вставки: ")

    with open('new_poem.txt', 'w', encoding='utf-8') as new_poem_file:
        lines = content.split('\n')
        n = int(input("Введите номер строки N: "))
        for i, line in enumerate(lines):
            new_poem_file.write(line + '\n')
            if i == n-1:
                new_poem_file.write(user_phrase + '\n')

print(f"Количество пробельных символов в файле: {space_count}")
