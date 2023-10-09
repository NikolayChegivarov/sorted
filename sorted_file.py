import glob
import os
# Использую glob для получения списка всех файлов с расширением .txt
# с указанием текущей дериктории
filenames = glob.glob(os.path.join(os.getcwd(), '*.txt'))
# Помещаю в filenames список имен файлов, убераю путь.
filenames = [os.path.basename(file) for file in filenames]

files_name_str = {}
for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as file:
        # Хочу получить словарь - [названия файлов : строки в списке]
        files_name_str[filename] = file.read().splitlines()

# Сортирую словарь по количеству строк в файле
sorted_files_data = dict(sorted(files_name_str.items(), key=lambda item: len(item[1])))
print(sorted_files_data)
# Записываю отсортированный словарь в новый файл
with open('output.txt', 'w', encoding='utf-8') as output_file:
    for filename, lines in sorted_files_data.items():
        output_file.write(filename + '\n')
        output_file.write(str(len(lines)) + '\n')
        output_file.write('\n'.join(lines) + '\n\n')











