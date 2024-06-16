Программа, объединяющая файлы в один и сортирующая по следующим правилам:
1. Содержимое исходных файлов в результирующем файле сортируется по количеству строк в них (первым записывается файл с наименьшим количеством строк, а последним - с наибольшим)
2. Содержимому файла предшествует служебная информация на 2 строках: имя файла и количество строк в нем

<br>

Пример: даны файлы
<br>
1.txt
```
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
```

2.txt
```
Строка номер 1 файла номер 2
```

Итоговый файл: 
```
2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1
```
