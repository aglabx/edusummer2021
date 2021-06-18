# Спринт2 21-27.06.2021

## Подготовка данных к формальной проверке

Для того, чтобы автоматизировать проверку заданий, задания должны быть оформлены стандартным способом.

На примере первой недели:

1. Путь к файлу должен быть вида **edusummer2021/students/<your gtihub name>/codewars/week1_solutions.md**
2. Файлы должны быть у правильное ветке week1 или week2 и тд.

Markdown файл должен быть следующего вида

``````md
  
# 1. Opposite Number. https://www.codewars.com/kata/56dec885c54a926dcd001095

```python
def opposite(number):
    return -1 * number
```
  
# 2. Even or Odd. https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

```python
def even_or_odd(number):
    return "Odd" if number % 2 else "Even"
```

``````
  
Хедер начинается с решетки. Потом номер задания, потом точка, потом имя задания, потом точка, внутри имени задания других точек не должно быть.
  Потом ссылка на ваше решение, если такая ссылка еть.

После этого пустая строка. 
  
Потом три лапки слово python. Внутри код. Обратите внимание на отступы, один отступ - это четыре пробела, никаких табов. Потом три лапки.
  
После этого пустая строка.
  
После этого следущее решение.
  
Без такого форматирование задание автоматически не примется.
  
## Биологические форматы данных.
  
## Работа с табличными файлами.

## Пишем свой парсер фасты.

## Пишем свой парсер gbff (со зведочкой).

## Вторая глава Кунина.

## Начинаем штурмовать биологическую часть Розалинда.
  
Задачки на эту неделю:
  
1. Let's Be Practical http://rosalind.info/problems/ini/
2. Four Commonly Used Protein Databases http://rosalind.info/problems/dbpr/
3. New Motif Discovery http://rosalind.info/problems/meme/
4. GenBank Introduction http://rosalind.info/problems/gbk/
5. Data Formats http://rosalind.info/problems/frmt/
6. FASTQ format introduction http://rosalind.info/problems/tfsq/
7. Read Quality Distribution http://rosalind.info/problems/phre/
8. Read Filtration by Quality http://rosalind.info/problems/filt/
9. Base Quality Distribution http://rosalind.info/problems/bphr/
10. Base Filtration by Quality http://rosalind.info/problems/bfil/

## Начинаем пробовать писать сортировки.
