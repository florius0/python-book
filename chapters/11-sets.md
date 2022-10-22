# 12. Работа с множествами (`set` и `frozenset`)

## 2. Типы-множества

Множества в Python – это неупорядоченные коллекции уникальных объектов.

### 1. `frozenset`

Иммутабельное множество

Не имеет литерала.

Конструкторы:

1. `frozenset()` – создает пустое множество
2. `frozenset(iterable)` – создает множество из элементов `iterable`. Каждый элемент должен быть хешируемым.

Для `frozenset` определены следующие операции:

| Операция                          | Результат                                                                                |
| --------------------------------- | ---------------------------------------------------------------------------------------- |
| `set.isdisjoint(other)`           | `True` если у `set` и `other` нет общих элементов , иначе `False`                        |
| `set.issubset(other)`             | `True` если все элементы `set` есть в `other` , иначе `False`                            |
| `set <= other`                    | Аналогично `set.issubset(other)`                                                         |
| `set < other`                     | `True` если все элементы `set` есть в `other` и `set` не равно `other` , иначе `False`   |
| `set.issuperset(other)`           | `True` если все элементы `other` есть в `set`, иначе `False`                             |
| `set >= other`                    | Аналогично `set.issuperset(other)`                                                       |
| `set > other`                     | `True` если все элементы `other` есть в `set` и `set` не равно `other`, иначе `False`    |
| `set.union(other, ...)`           | Новое множество с элементами `set` и `other`                                             |
| `set | other | ...`               | Аналогично `set.union(other, ...)`                                                       |
| `set.intersection(other, ...)`    | Новое множество с элементами которые есть в `set` и в `other`                            |
| `set & other & ...`               | Аналогично `set.intersection(other, ...)`                                                |
| `set.difference(other, ...)`      | Новое множество с элементами `set`, которых нет в `other`                                |
| `set - other - ...`               | Аналогично  `set.difference(other, ...)`                                                 |
| `set.symmetric_difference(other)` | Новое множество с элементами, которые есть только в `set` и `other`, но не в обоих сразу |
| `set ^ other`                     | Аналогично  `set.symmetric_difference(other)`                                            |
| `set.copy()`                      | Копия множества (копируется только множество, но не его элементы)                       |

Для некоторых методов определены соответствующие операторы. Аргументами операторов могут только множества, а методов – любые итерируемые объекты.

### 2. `set`

Мутабельное множество

Не имеет литерала.

Конструкторы:

1. `set()` – создает пустое множество
2. `set(iterable)` – создает множество из элементов `iterable`. Каждый элемент должен быть хешируемым.

Для `set` определены все те же операции, что и для `frozenset` и дополнительно определены следующие операции:

| Операция                                      | Результат                                                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `set.update(other, ...)`                      | Обновляет множество, добавляя все элементы из `other`                                                         |
| `set |= other | ...`                          | Аналогично `update(other, ...)`                                                                               |
| `set.intersection_update(other, ...)`         | Обновляет множество, сохраняя только те элементы, которые встречаются в `other`                               |
| `set &= other & ...`                          | Аналогично `intersection_update(other, ...)`                                                                  |
| `set.difference_update(other, ...)`           | Обновляет множество, сохраняя только те элементы, которые не встречаются в `other`                            |
| `set -= other | ...`                          | Аналогично `difference_update(other, ...)`                                                                    |
| `set.symmetric_difference_update(other, ...)` | Обновляет множество, сохраняя только те элементы, которые есть только в `set` и `other`, но не в обоих сразу |
| `set ^= other`                                | Аналогично `symmetric_difference_update(other, ...)`                                                          |
| `set.add(elem)`                               | Добавляет элемент в множество                                                                                 |
| `set.remove(elem)`                            | Удаляет элемент из множества. Если элемента в множестве нет – вызывает `KeyError`                            |
| `set.discard(elem)`                           | Удаляет элемент из множества.                                                                                 |
| `set.pop()`                                   | Возвращает произвольный элемент множества и удаляет его из множества                                          |
| `set.clear()`                                 | Удаляет все элементы множества                                                                                |