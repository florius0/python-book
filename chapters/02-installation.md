# 2. Установка

Мы будем использовать Python 3.8+ (версии 3.8 и старше)

## Windows

1. Скачайте установщик последней доступной версии с официального сайта Python: <https://www.python.org/downloads/>
2. Запустите скачанный установщик

## Linux

На большинстве Linux-дистрибутивах Python должен быть установлен по умолчанию, проверить версию можно при помощи команды `python3 -V`.

Если ваша версия Python устарела или `python3` отсутствует, то воспользуйтесь приведенными ниже инструкциями для популярных дистрибутивов.

### Дистрибутивы, основанные на Debian

Выполните следующие команды в терминале

```bash
sudo apt-get update
sudo apt-get install python3
```

### Дистрибутивы, основанные на Arch

Выполните следующие команды в терминале

```bash
sudo install pacman -S python
```

Если вашего дистрибутива нет в списке, найдите инструкцию по установке/обновлению Python'а для вашего дистрибутива в интернете

## macOS

Совремменные версии macOS включают в себя python3 по умолчанию. Проверить версию можно при помощи команды `python3 -V`.

Если ваша версия Python устарела или `python3` отсутствует, рекомендуется установка через пакетный менеджер `homebrew`:

Выполните следующие команды в терминале

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3
```