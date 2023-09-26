import requests
import json


def api(path): # парсинг данных
    data = requests.get(path).json()
    return data

def open_file(path): # открытие файла
    with open(path, 'r') as r:
        return json.load(r)


def dictionary(): # словарь
    uniq_replacement = {}

    for replacement in reversed(open_file('replacement.json')):
        replacement['source'] = replacement['source'] or ""  # Замена none на пустую строку
        uniq_replacement.setdefault(replacement['replacement'], replacement)

    return uniq_replacement


def source_text(): # получение исходного текста
    data = api('https://raw.githubusercontent.com/thewhitesoft/student-2023-assignment/main/data.json')

    uniq_replacement = dictionary()
    updated_data = []

    for item in data:
        for key, replacement in uniq_replacement.items(): # используем два значения, для избежания ошибок со строкой
                item = item.replace(replacement['replacement'], replacement['source'])
        updated_data.append(item)
        
    return updated_data


def save_source_text(): # сохранения исходного текста
    updated_data = source_text()
    lines_list = []

    for item in updated_data:
        lines_list.extend([line for line in item.split('\n') if line.strip()]) # удаление пустых строк

    with open('result.json', 'w') as result:
        try:
            json.dump(lines_list, result, ensure_ascii=False, indent=4)
            print ('Текст успешно восстановлен и сохранен!')
        except Exception as e:
            print (f'Ошибка - {e}')


if __name__ == '__main__':
    save_source_text()