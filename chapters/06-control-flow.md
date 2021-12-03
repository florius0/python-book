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

где – `condition1` и `condition2` – выражения, которые при необходимостси автоматически преобразуются к `bool`

В результате выполнения вышепреведенной програмы получим:

<!--
runs: chapter_6/if_elif.py
-->

```bash
1
```

Нетрудно заметить, что `elif` – эквивалент `else: ... if`:

<!-- 
filename: chapter_6/if_else_if.py
-->

```python
condition1 = True
condition2 = True

if condition1:
    # Блок будет выполнен если `condition1` – истинно
    print(1)
else:
    if condition2:
        # Блок будет выполнен если `condition1` – ложно и `condition2` – истинно
        print(2)
    else:
        # Блок будет выполнен во всех остальных случаях
        print(3)
```

В результате выполнения получим то же, что и при использовании `elif`:

<!--
runs: chapter_6/if_else_if.py
-->

```bash
1
```

В `if` может быть произвольное количество `elif`-частей (в том числе и не быть вообще). `else`-часть – опциональна.

## 2. Циклы

### 1. `for`

Записывается при помощи ключевых слов `for` и `in`.

<!-- 
filename: chapter_6/for.py
-->

```python
iterable = 'abcdefg'
for variable in iterable:
    # Блок-тело цикла, выполняется для каждого элемента `iterable`
    # `variable` – переменная, равная текущему элементу `iterable`
    print(variable)
```

где `iterable` – любой итерируемй объект.

В результате выполнения получим

<!-- 
filename: chapter_6/for.py
-->

```python
a
b
c
d
e
f
g
```

### 2. `while`

Записывается при помощи ключевого слова `while`

<!-- 
filename: chapter_6/while.py
-->

```python
condition = True
while condition:
    # Блок–тело цикла, выполняется пока `condition` истинно
    print(1)

    # При следующей итерации цикла `condition` будет ложно и произойдет выход из цикла
    condition = False
```

Где `condition` – выражение, которые при необходимостси автоматически преобразуются к `bool` (точно так же, как и `condition1` и `condition2` в `if`)

В результате получим:

<!-- 
runs: chapter_6/while.py
-->

```bash
1
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

Запустив программу, получим

<!-- 
runs: chapter_6/for_else.py
-->

```bash
2
```

### Ключевое слово `break`

`break` досрочно прерывает цикл, внутри блока которого `break` исполнится:

<!-- 
filename: chapter_6/break.py
-->

```python
for i in range(1, 11):
    print(i)
    break
```

Результат запуска программы:
<!-- 
runs: chapter_6/break.py
-->

```bash
1
```

<!-- 
filename: chapter_6/break_with_condition.py
-->

```python
for i in range(1, 11):
    if i > 5:
        print('break')
        break

    print(i)
```

Результат запуска программы:
<!-- 
runs: chapter_6/break_with_condition.py
-->

```bash
1
2
3
4
5
break
```

<!-- 
filename: chapter_6/break_nested.py
-->

```python
while True:
    for i in range(1, 11):
        print(i)

        # Прервет цикл `for`
        break
    
    # Прервет цикл `while`
    break
```

Получим:

<!-- 
runs: chapter_6/break_nested.py
-->

```bash
1
```

### Ключевое слово `continue`

`continue` начинает следующую итерацию цикла, внтури блока которого `continue` исполнится:

<!-- 
filename: chapter_6/continue.py
-->

```python
for i in range(1, 11):
    if i < 5:
        continue

    print(i)
```

В результате имеем

<!-- 
runs: chapter_6/continue.py
-->

```bash
5
6
7
8
9
10
```

### Ключевое слово `pass`

`pass` не делает ничего. Используется когда синтаксически требуется какая-то инструкция, но в программе не требуется совершить какое-либо действие:

<!-- 
filename: chapter_6/pass.py
-->

```python
for i in range(1, 11):
    # Только проитерирует `range(1, 11)`
    pass
```
