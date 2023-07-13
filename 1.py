# Напишите функцию, которая получает на вход директорию и рекурсивно обходит 
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в 
# ней с учётом всех вложенных файлов и директорий.

import os
import json
temp_dict = {}

def look_into_dir(list_of_obj: list) -> dict:
   
    for obj in list_of_obj:
        print(f'{os.path.isdir(obj) = }', end='\t')
        print(f'{obj = }')
        if os.path.isdir(obj) == True and obj != ".git":
            file_1 = os.path.join(os.getcwd(), f'{obj}')
            size = os.path.getsize(file_1)
            result = {"Is a directory": size}
            temp_dict[obj] = result

            os.chdir(file_1)

            dir2_list = os.listdir()

            look_into_dir(dir2_list)

            os.chdir('../')
        else: 
            file_1 = os.path.join(os.getcwd(), f'{obj}')
            size = os.path.getsize(file_1)
            result = {"Is a file": size}
            temp_dict[obj] = result

        print(temp_dict)
    return temp_dict

def write_into_json(temp_dict: dict, name_file: str) -> None:
    with open(name_file, 'w', encoding='utf-8') as f_write:
            json.dump(temp_dict, f_write, ensure_ascii=False, indent=2)
    
       
if __name__ == '__main__':

    print("-------------")
    print(os.getcwd())
    dir_list = os.listdir()
    temp_dict = look_into_dir(dir_list)
    write_into_json(temp_dict, "test.json")
    print("-------------")