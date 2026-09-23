# vpv04-konstsherbakov

## Что это

Учебный Python-скрипт: отправляет запрос на google.com и выводит код ответа сервера. Цель — освоить VS Code, виртуальное окружение и Git.

## Как запустить

1. Клонировать репозиторий: `git clone https://github.com/konstsherbakov/vpv04-konstsherbakov.git`
2. Перейти в папку: `cd vpv04-konstsherbakov`
3. Создать виртуальное окружение: `python -m venv .venv`
4. Активировать его (Windows PowerShell): `.venv\Scripts\Activate.ps1`
5. Установить зависимости: `pip install -r requirements.txt`
6. Запустить: `python main.py`

## Как проверить, что работает

В терминале появятся строки `Hello, World!` и `Status code from https://google.com: 200`. Код 200 означает, что сервер ответил успешно. Эталонный вывод лежит в `examples/sample_output.txt`.

## Что я сделал в этом уроке

- Настроил VS Code и виртуальное окружение .venv
- Установил библиотеку requests и написал HTTP-запрос
- Создал Git-репозиторий и опубликовал его на GitHub
- Доработал вывод скрипта и добавил .gitignore, requirements.txt и пример вывода

## Что было сложным / что понял

Сложнее всего было разобраться, где Python, а где команды терминала PowerShell: я вставлял код Python в терминал и получал ошибки. Ещё запутался из-за двух виртуальных окружений в одной папке. Понял логику Git: add собирает изменения, commit фиксирует их локально, push отправляет на GitHub.