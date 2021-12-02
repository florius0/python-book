# 6. Управление потоком

До сих пор мы рассматривали только программирование линейныых алгоритмов.

## 1. Ветвления

В Python есть только один тип ветвлений – `if`

Записываются при помощи ключевых слов `if`, `else` и `elif`:

<!-- 
filename: chapter_6/if_elif.py
-->

```python
condition1 = True
condition2 = True

if condition1:
    # Блок будет выполнен если condition1 – истинно
    print(1)
elif condition2:
    # Блок будет выполнен если condition1 – ложно и conddition2 – истинно
    print(2)
else:
    # Блок будет выполнен во всех остальных случаях
    print(3)
```

где – `condition1` и `condition2` – выражения-условия, которые при необходимостси автоматически преобразуются к `bool`

Нетрудно заметить, что `elif` – эквивалент `else if`:

<!-- 
filename: chapter_6/if_else_if.py
-->

```python
condition1 = True
condition2 = True

if condition1:
    # Блок будет выполнен если `condition1` – истинно
    print(1)
else if condition2:
    # Блок будет выполнен если `condition1` – ложно и `condition2` – истинно
    print(2)
else:
    # Блок будет выполнен во всех остальных случаях
    print(3)
```

В `if` может быть произвольное количество `elif`-частей (в том числе и не быть вообще). `else`-часть – опциональна.

## 2. Циклы

### 1. `for`

Записывается при помощи ключевых слов `for` и `in`.

```python
iterable = 'abcdefg'
for variable in iterable:
    # Блок-тело цикла, выполняется для каждого элемента `iterable`
    # `variable` – переменная, равная текущему элементу `iterable`
    print(variable)
```

где `iterable` – любой итерируемй объект.

### 2. `while`

Записывается при помощи ключевого слова `while`

```python
condition = True
while condition:
    # Блок–тело цикла, выполняется пока `condition` истинно
    print(1)

    # При следующей итерации цикла `condition` будет ложно и произойдет выход из цикла
    condition = False
```

### `else`-часть циклов

У всех циклов может быть `else`-часть – блок которой будет выполнен если цикл совершил 0 итераций:

<!--
filename: chapter_6/for_else.py
-->

```python
for i in []:
    print(1)
else:
    print(2)
```

### Ключевое слово `continue`

### Ключевое слово `break`

### Ключевое слово `pass`
