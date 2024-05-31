file_names = ["1.txt", "2.txt", "3.txt"]

# Создаем список для хранения содержимого каждого файла
content_list = []

# Считываем содержимое каждого файла и добавляем его в список content_list
for file_name in file_names:
    with open(file_name, 'r', encoding="utf8") as file:
        content = file.readlines()

        content_list.append((len(content), file_name, content))


content_list.sort(key=lambda x: x[0])


with open("result.txt", 'w') as result_file:

    for num_lines, file_name, content in content_list:
        result_file.write(f"{file_name}\n{num_lines}\n")
        result_file.write(''.join(content))