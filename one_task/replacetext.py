import requests
import sys
import json


def api(path): #  сбор данных
    try:
        data = requests.get(path).json()
        return data
    except ValueError:
        print ('Произошла ошибка, при указание ссылки!')
        sys.exit()


def open_file(path): #  открытие файла
    try:
        with open(path, 'r') as r:
            return json.load(r)
    except FileNotFoundError as e:
        print (f'Произошла ошибка, при указание пути файла: {e}')
        sys.exit()


def dictionary(f_path): #  словарь
    uniq_replacement = {}

    for replacement in reversed(open_file(f_path)):
        replacement['source'] = replacement['source'] or ""  # Замена none на пустую строку
        uniq_replacement.setdefault(replacement['replacement'], replacement)

    return uniq_replacement


def source_text(data, f_path): #  получение исходного текста

    uniq_replacement = dictionary(f_path)
    updated_data = []

    for item in data:
        for key, replacement in uniq_replacement.items(): # используем два значения, для избежания ошибок со строкой
                item = item.replace(replacement['replacement'], replacement['source'])
        updated_data.append(item)
        
    return updated_data


def save_source_text(data, f_path): #  сохранение исходного текста
    lines_list = []
    updated_data = source_text(data, f_path)

    for item in updated_data:
        lines_list.extend([line for line in item.split('\n') if line.strip()]) # удаление пустых строк

    with open('result.json', 'w') as result:
        try:
            json.dump(lines_list, result, ensure_ascii=False, indent=4)
            print ('\nТекст успешно восстановлен и сохранен!')
        except Exception as e:
            print (f'Ошибка - {e}')


def data_input(): #  указывание путей
    data = api(input('Привет!\nВставьте ссылку для сбора информации с сайта: '))
    f_path = str(input('Напиши путь до json файла: '))
    save_source_text(data, f_path)

    return data, f_path


if __name__ == '__main__':
    data_input()