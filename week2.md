# Спринт2 21-01.07.2021

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
  
Ccылка тут: https://github.com/aglabx/edusummer2021/blob/main/biological_formats.md

## Пишем свой парсер фасты.

Сделайте папочку playgroung, мы в ней начнем писать вашу лучную библиотеку для биоинформатики.
  
Задача реализовать следующее решение, файл **playgroung/fasta_reader.py**:
  
```python
  
def stupid_fasta_reader(fasta_file_name):
    """ Write here the correct doc string.
    """
    sequences = []
    ...
    return sequences

def iter_fasta_file(fasta_file_name):
    """ Write here the correct doc string.
    """
    ...
    yield header, sequence
  
  
class FastaData:
    ...
    def _parse_header(self):
        """ Write here the correct doc string.
        """
        ...
    ...

  
def iter_fasta_objects(fasta_file_name):
    """ Write here the correct doc string.
    """
    ...
    seq_obj = FastaData...
    ...
    yield seq_obj
 
```
  
Написать абстрактный ридер блочных файлов на основе кода фаста ридера с классами и без, файл **playgroung/block_reader.py**.
  
```python

class BlockData:
  ...
  
  
def iter_block_objects(blocks_file_name, new_block_symbol):
  """ Write here the correct doc string.
  """
  ...
  block_obj = BlockData...
  ...
  yield block_obj


def iter_block_file(blocks_file_name, new_block_symbol):
    """ Write here the correct doc string.
    """
    ...
    yield header, data
```
  
Перепишите FastaData класс наследовав его от BlockData, тоже в файле **playgroung/fasta_reader.py**:
  
```python
class FastaData(BlockData):
    ...
```

Теперь у нас есть всё, чтобы легко написать парсер для FastQ файла, сначала напишите решение в лоб, а потом напишите красивый класс.
  
Это будет основой следующего спринта, когда будем FastQC свой писать, чтобы разобраться в его самых страшных секретах, файл **playgroung/fastq_reader.py**

```python
 
 def iter_fastq_file(fastq_file_name):
    """ Write here the correct doc string.
    """
    ...
    yield header, sequence, strand, quality_string
  
class FastqData(BlockData):
    ...
    def _parse_header(self):
        # воспользуйтесь документацией иллюмины
        ...
    
    def _convert_phred_to_probability(self):
        ...
  
def iter_fastq_blocks(fastq_file_name):
    """ Write here the correct doc string.
    """
    ...
    yield fastq_obj
 
```
  
Документация по классам: https://docs.python.org/3/tutorial/classes.html

## Работа с табличными файлами.
  
Задача уметь читать и писать:
  
1. csv files
2. tsv files
3. bed files
4. gff3 files
5. sam files
6. vcf files
  
Для первых двух есть отличная библиотека https://docs.python.org/3/library/csv.html
  
Для остальных в лоб ее использовать не получится. Так как в них часто запихнуты не табличные данные.

Сейчас ваша задача разобраться какие в этих файлах есть поля. А это проще всего сделать имплементиров ридеры для этих файлов.
  
Начнем опять с абстрактного контейнера, чтобы не повторять себя в коде много раз, , файл **playgroung/tsv_readers.py**
  
На этом этапе вам нужно составить только поля из соответствующих форматов, к усоврешенствованию этих классов мы еще много раз вернемся.
Так что минимум придется доки по форматам найти и прочитать.
  
```python

class TabDelimitedData:
   def __init__(self):
       ... 
  
class BEDData(TabDelimitedData):
   def __init__(self):
       ...

class GFF3Data(TabDelimitedData):
   def __init__(self):
       ...
  
class SAMData(TabDelimitedData):
   def __init__(self):
       ...

class VCFData(TabDelimitedData):
   def __init__(self):
       ...
  
```
  
Попробуйте найти в этих данных общее и вынести это в родительский класс.
  
При имплементации нужно решить следующие задачи будет, сейчас это задачка со зведочкой (*):
  
1. Есть 0- и 1-based файлы, нужно научиться конвертировать туда обратно, как это лучше сделать?
2. Если значение число, то оно и должно возвращаться, как это лучше сделать.
3. Часть значение это словари как из развернуть? Для части полей значения могут быть списками, а как это сделать?
4. Возможно ли придумать как описывать поля, чтобы можно было легко менять базовые классы под новые форматы?
  
## Пишем свой парсер gbff (со зведочкой).

Умея читать блочные файлы, чтения злобных форматов по типа генбанка уже не что-то сложное:
  
```python
  
class GBFFData(BlockData):
    ...
    def __init__(self):
        ... 
        self.sequence = ...
        self.header = ...
        self.length = ...
        self.taxon = ...
   ...
  
def iter_gbff_blocks(gbff_file_name):
    """ Write here the correct doc string.
    """
    ...
    yield gbff_obj
```
  
## Вторая глава Кунина.

Во-первых, нужно пройти тест по первой главе Кунина. И конспект второй главы в виде терминов разбитых на группы.

Группы: 
  
1. Ясно и могу объяснить.
2. Вроде ясно, но не уверен, что смогу объяснить своими словами.
3. Не ясно, нужна помощь с пониманием.

Кроме терминов, еще нужно придумать **три** вопроса, которых еще нет в списке вопросов придуманных.

Не откладывайте Кунина, он сложней, чем может показываться.

  
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
  
Часть решений смело добавляйте в классы, что мы пишем для чтения фасты и фастку.
  
## Задачки с codewars для разогрева

Задачки из слака яндекс практики по алгоритмам. Расчитаны на неделю.
  
Для каждой задачки нужно попробовать оценить сложность время/память. 
  
Статья вам в помощь https://habr.com/ru/post/444594/ и тут https://www.programiz.com/dsa/asymptotic-notations, 
кроме этого первая лекция яндекса. Вы же я надеюсь их смотрите?
  
Еще две ссылки https://medium.com/dataseries/a-quick-primer-on-big-o-notation-c99ccc7ddbae и https://medium.com/dataseries/how-to-calculate-time-complexity-with-big-o-notation-9afe33aa4c46
  
### 2.1. Human Readable Time kyu5

https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

### 2.2. Isograms kyu7
https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

### 2.3. Categorize New Member kyu7
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

### 2.4. Vasya - Clerk kyu6
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

### 2.5. The Supermarket Queue kyu6
https://www.codewars.com/kata/57b06f90e298a7b53d000a86

## Задачки с codewars по теме работа с циклами

### 2.6. Sum of a sequence kyu7
https://www.codewars.com/kata/586f6741c66d18c22800010a

### 2.7. Sum of a Beach kyu7
https://www.codewars.com/kata/5b37a50642b27ebf2e000010

### 2.8. Alphabet war kyu7
https://www.codewars.com/kata/59377c53e66267c8f6000027

### 2.9. Create Phone Number kyu6
https://www.codewars.com/kata/525f50e3b73515a6db000b83

### 2.10. Rot13 kyu5
https://www.codewars.com/kata/530e15517bc88ac656000716

### 2.11. Strip Comments kyu4
https://www.codewars.com/kata/51c8e37cee245da6b40000bd

  
## Вторая неделя яндекса (ползвёздочки)
  
Попробуйте решить их. Они значительно проще чем первая неделя.
