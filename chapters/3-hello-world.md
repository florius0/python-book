# 3. Hello World

При знакомстве с новыми языками программирования принято в качестве первой программы писать программу Hello World, которая печатает "Hello World".

Исходный код Python сохраняют в файлах с расширением `.py`.

Для запуска программы на Python следует открыть терминал и ввести команду `python3 <filename>` (`python <filename>` на Windows), где `<filename>` нужно заменить на путь к файлу с исходным кодом.

1. Создайте файл `chapter_1/hello_world.py` со следующим содержанием. обратите внимание, что в Python (согласно [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)) принято оставлять пустую строку в конце файла.
<!--
filename: chapter_1/hello_world.py
-->

```python
print("Hello World!")

```

2. Запустите программу при помощи команды `python3 chapter_1/hello_world.py`. Последние 3 строки вашего терминала должны выглядеть примерно так:

<!-- 
runs: chapter_1/hello_world.py
stdin: ''
stdout: >
    Hello World!
-->

```bash
> python3 chapter-1/hello-world.py
Hello World!
>
```
