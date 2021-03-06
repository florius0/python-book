# 4. Структура программы и переменные

## Структура программы

Программа на Python состоит из блоков. Блок – произвольное количество кода с определенным отступом:

```python
# блок
print('a')
print(1 + 2)

for i in range(10):
    # блок
    print(i)
```

Принято в качесве символов отступа использовать пробелы (большинство редакторов заменяют символ табуляции на пробелы) и делать отступ, кратный четырем пробелам.

## Переменные

Python – императивный язык (исходный код состоит из упорядоченных инструкция), и как и в других императивных языках, переменная – "коробочка", в которой находится какое-либо значение.

В Python переменная – это произвольное имя, которое является ссылкой на какой либо объект.

Имя переменной:

- может содержать буквы, цифры и знак подчеривания (`_`)
- не может начинаться с цифры
- не может совпадать с одним из ключевых слов: `None`, `False`, `True`, `in`, `and`, `or`, `is`, `not`, `as`, `lambda`, `class`, `def`, `pass`, `return`, `if`, `elif`, `else`, `while`, `for`, `continue`, `break`, `yield`, `async`, `await`, `global`, `nonlocal`, `del`, `import`, `from`, `raise`, `try`, `except`, `finally`, `with`, `assert`

Переменная всегда имеет какое-либо значение. Чтобы объявить переменную, достаточно присвоить имени какое-либо значение:

<!-- 
filename: chapter_4/variables_1.py
-->

```python
a = 1 + 2

print(a)
```

Выведет:

<!--
runs: chapter_4/variables_1.py
-->

```bash
3
```

Так же можно объявить перерменные цепочкой:

<!-- 
filename: chapter_4/variables_2.py
-->

```python
a = b = 10

print(a)
print(b)
```

Выведет:

<!--
runs: chapter_4/variables_2.py
-->

```bash
10
10
```

## Типизация в Python

Типизация бывает:

- Сильная или слабая (строгая или не строгая). Если типизация сильная, то язык не позволяет смешивать в одном выражении различные типы и не выполняет автоматические преобразовния типов.
- Явная или неявная. Если типизация явная, то типы (функций, переменных, аргументов и. т. д) должны быть указаны явно.
- Статическая или динамическкая. Если типизация динамическая, то переменная связывается с каким-либо типом только в момент присваивания значения, таким образом одна и та же переменная в разных местах может иметь значения разных типов. Если типизация статическая, то переменная связывается с каким-либо типов в момент объявления, и ее тип не может быть изменен позже.

Python – язык с сильной неявной динамической типизацией.

## Объекты

Python – объектно-оринтированный язык. Практически все в Python – объект.

Объект – некоторая сущность, обладающая определенным состоянием и поведение, имеющая определенные свойства – аттрибуты и операции – методы. Каждый объект – экземпляр какого либо класса. Тип объекта – класс, экземпляром которого он является. В Python есть функция `type(object)`, которая возвращает тип своего аргумента.

```python
# Выведет значение какого-то аттрибута `attribute` у объекта `o`
print(o.attribute)

# Выведет значение, которое вернет метод `method` у объекта `o`
print(o.method())

# Выведет тип объекта `o`
print(type(o))
```

Подробнее мы рассмотим объекты и классы в 6 главе.

## Ссылки на объекты

Мы уже говорили, что в Python переменная – это ссылка на объект.
Когда мы присваиваем переменной что-то, допустим

```python
n = 300
```

Python создаст объект `300` и `n` будет ссылкой на этот объект:

![`n` ссыылается на `300`](./04-program-structure-and-variables/1.png)

Если мы присвоим `n` переменной `m`:

```python
m = n
```

`m` будет ссылкой на `300`:

![`n` и `m` ссыылаются на `300`](./04-program-structure-and-variables/2.png)

Теперь 400 присвоим `m`:

```python
m = 400
```

Python создаст новый объект `400` и `m` будет ссылкой на этот объект:

![`n` ссыылается на `300`, `m` – на `400`](./04-program-structure-and-variables/3.png)

Теперь `"foo"` присвоим `n`:

```python
n = "foo"
```

Python создаст новый объект `"foo"` и `n` будет ссылкой на этот объект, а на объект `300` ссылок не будет, соотвтетственно не будет и способа получить объект `300`:

![`n` ссыылается на `"foo"`, `m` – на `400`, на `300` ссылок нет](./04-program-structure-and-variables/4.png)

Если количество ссылок на какой либо объет будет равным нулю, `Python` удалит этот объект. Этот процесс называется сборкой мусора или garbage collection (GC). `Python` не гарантирует, в какой момент времени после достижения нулевого количества ссылок объет будет удален.

Жизненным циклом объекта называется промежуток времени от его создания до момента достижения нулевого количества ссылок (иногда говорят удаления, но это не совсем верно).
