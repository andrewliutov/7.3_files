my_list = ['1.txt', '2.txt', '3.txt']
early_list = []

for i in my_list:
    my_dict = {}
    with open(i, 'r', encoding='utf-8') as file:
        my_dict['Имя файла'] = i
        lines = file.readlines()
        my_dict['Количество строк'] = int(len(lines))
        my_dict['Содержимое файла'] = lines
        early_list.append(my_dict)

result_list = sorted(early_list, key=lambda x: x['Количество строк'])

with open('4.txt', 'w', encoding='utf-8') as file_target:
    for element in result_list:
        p = str("".join(element['Содержимое файла']))
        file_target.write(f"{str(element['Имя файла'])} "
                          f"\n{str(element['Количество строк'])} \n{p} \n")
