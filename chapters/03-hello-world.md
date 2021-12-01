# 3. Hello World

При знакомстве с новыми языками программирования принято в качестве первой программы писать программу Hello World, которая печатает "Hello World".

Исходный код Python сохраняют в файлах с расширением `.py`.

Для запуска программы на Python следует открыть терминал и ввести команду `python3 <filename>` (`python <filename>` на Windows, в дальнейшем мы будем везде писать `python3`), где `<filename>` нужно заменить на путь к файлу с исходным кодом.

## Hello World

1. Создайте файл `chapter_1/hello_world.py` со следующим содержанием. обратите внимание, что в Python (согласно [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)) принято оставлять пустую строку в конце файла.

<!--
filename: chapter_3/hello_world.py
-->

```python
print('Hello World!')

```

2. Запустите программу при помощи команды `python3 chapter_1/hello_world.py`. Последние 3 строки вашего терминала должны выглядеть примерно так:

<!-- 
runs: chapter_3/hello_world.py
stdin: ''
stdout: >
    Hello World!
-->

```bash
> python3 chapter-1/hello-world.py
Hello World!
>
```

## Разбор примера

В этом примере мы воспользовались функцией [`print`](https://docs.python.org/3/library/functions.html#print), которая принимает произвольное количество аргументов и печатает их в `STDOUT`. Так же `print` принимает keyword-аргумент (или именованные аргументы) `sep` – разделитель, который будет использоан при печати аргументов и `end` – то, что будет выведено после всех аргументов. По умолчанию `sep=' '` и `end='\n`.

В качестве аргумента мы передали `'Hello World!'` – строку, заданную _литералом_ (_строковый литерал_). Подробнее мы рассмотрим строки, литералы и строковые литералы в следющей главе.

## Hello anything

Предположим, мы хотим поприветствовать не мир, а что-то другое. Конечно, мы можем написать другую программу, но это не разумно. Вместо этого мы воспользуемся функцией [`input`](https://docs.python.org/3/library/functions.html#input), которая читает все, что передано в `STDIN` до символа новой строки. Так же, `input` опционально принимает один аргумент – `prompt` – приглашение для ввода. `prompt` будет вывеен в `STDOUT` без символа новой строки.

1. Создайте файл `chapter_1/hello_anything.py` со следующим содержанием. обратите внимание, что в Python (согласно [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)) принято оставлять пустую строку в конце файла.

<!--
filename: chapter_3/hello_anything.py
-->

```python
print('Hello,', input())

```

2. Запустите программу при помощи команды `python3 chapter_1/hello_world.py`:

<!-- 
runs: chapter_3/hello_anything.py
stdin: 'Joe'
stdout: >
    Hello, Joe
-->

```bash
> python3 chapter-1/hello_anything.py
Joe
Hello, Joe
>
```

## Задания

1. Разберите `chapter_1/hello_anything.py`
2. Поэкспереминтируйте с аргументами функции `print` и добейтесь, чтобы в `chapter_1/hello_anything.py` выводился воскклицательный знак без пробела в конце строк: `Hello, Joe!`
3. Добавьте приглашение `Input your name:` для ввода имени. После двоеточия должен стоять пробел.
