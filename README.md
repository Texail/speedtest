# Internet Speed Test CLI

[RU](#ru-language) [ENG](#eng-language)

---

<a name="ru-language"></a>

## 📡 Internet Speed Test

Простая консольная утилита на Python для измерения скорости скачивания файла по указанному URL.

Программа последовательно выполняет несколько HTTP-запросов, полностью скачивает файл, измеряет время каждого запроса и рассчитывает среднюю скорость загрузки.

Проект использует [Requests](https://requests.readthedocs.io/) и запускается через [uv](https://docs.astral.sh/uv/).

## ✨ Возможности

- 🔗 Принимает URL файла для скачивания.
- 🔄 Выполняет 10 последовательных запросов по умолчанию.
- ⏱️ Измеряет время каждого запроса.
- 📦 Подсчитывает объём загруженных данных.
- ⚡ Рассчитывает скорость каждого запроса.
- 📊 Выводит среднее время и среднюю скорость.
- 💾 Использует потоковое скачивание (`stream=True`), поэтому файл целиком не загружается в оперативную память.
- ⚙️ Позволяет изменить количество запросов через аргумент командной строки.

## 🛠️ Требования

- Python **3.9+**
- [uv](https://docs.astral.sh/uv/)

Дополнительная ручная установка зависимостей не требуется: `uv` автоматически установит `requests` согласно метаданным в начале файла.

## 🚀 Запуск

### Вариант 1 — через `uv run`

Скачайте репозиторий:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Запустите программу:

```bash
uv run speed_test.py https://example.com/file.jpg
```

По умолчанию программа выполнит **10 последовательных запросов**.

### Количество запросов

Количество итераций можно изменить с помощью `-n` или `--iterations`:

```bash
uv run speed_test.py https://example.com/file.jpg -n 20
```

или:

```bash
uv run speed_test.py https://example.com/file.jpg --iterations 20
```

## 📋 Пример использования

```bash
uv run speed_test.py https://example.com/large-file.zip
```

Пример вывода:

```text
🚀 Начинаем замер скорости для: https://example.com/large-file.zip
🔄 Будет выполнено 10 последовательных запросов...

[01/10] ⏱️ 1.284 сек | 📦 25.00 MB | ⚡️ 19.47 MB/s
[02/10] ⏱️ 1.190 сек | 📦 25.00 MB | ⚡️ 21.01 MB/s
[03/10] ⏱️ 1.231 сек | 📦 25.00 MB | ⚡️ 20.31 MB/s
...
[10/10] ⏱️ 1.205 сек | 📦 25.00 MB | ⚡️ 20.75 MB/s

=============================================
📊 ИТОГОВЫЕ РЕЗУЛЬТАТЫ:
📥 Всего скачано:          250.00 MB
⏱️ Среднее время запроса:  1.221 сек
⚡️ Средняя скорость:       20.47 MB/s (Мегабайт/с)
=============================================
```

## 🧠 Как это работает

Для каждого запроса программа:

1. Запоминает время начала операции.
2. Выполняет HTTP GET-запрос.
3. Проверяет HTTP-статус ответа.
4. Скачивает ответ частями по **64 КБ**.
5. Подсчитывает количество полученных байт.
6. Измеряет общее время скачивания.
7. Рассчитывает скорость:

```text
скорость = объём данных / время
```

После завершения всех запросов программа рассчитывает средние показатели:

```text
среднее время = общее время / количество запросов
```

```text
средняя скорость = общий объём данных / общее время
```

## 📦 Почему используется `stream=True`

Вместо загрузки всего файла в память программа получает данные частями:

```python
requests.get(url, stream=True)
```

Затем файл читается блоками:

```python
for chunk in response.iter_content(chunk_size=65536):
    downloaded_bytes += len(chunk)
```

Это позволяет тестировать большие файлы без необходимости хранить их полностью в оперативной памяти.

## ⚠️ Важные особенности

Результат зависит не только от вашего интернет-соединения.

На измерение могут влиять:

- сервер, с которого скачивается файл;
- расстояние до сервера;
- загрузка сервера;
- CDN;
- сетевой маршрут;
- VPN или прокси;
- Wi-Fi вместо Ethernet;
- другие устройства и приложения, использующие сеть.

Поэтому для более стабильного результата рекомендуется использовать достаточно большой файл, расположенный на быстром сервере.

Все зависимости указаны непосредственно в `speed_test.py` в формате, поддерживаемом `uv`.

---

<a name="eng-language"></a>

## 📡 Internet Speed Test

A simple Python command-line utility for measuring download speed from a specified URL.

The program performs several sequential HTTP requests, fully downloads the file, measures the duration of each request, and calculates the average download speed.

The project uses [Requests](https://requests.readthedocs.io/) and can be run with [uv](https://docs.astral.sh/uv/).

## ✨ Features

- 🔗 Accepts a file URL as an argument.
- 🔄 Performs 10 sequential requests by default.
- ⏱️ Measures the duration of every request.
- 📦 Calculates the amount of downloaded data.
- ⚡ Calculates the speed of each request.
- 📊 Displays the average request time and average download speed.
- 💾 Uses streaming downloads (`stream=True`) to avoid loading the entire file into memory.
- ⚙️ Allows changing the number of requests from the command line.

## 🛠️ Requirements

- Python **3.9+**
- [uv](https://docs.astral.sh/uv/)

No manual dependency installation is required. `uv` automatically installs `requests` based on the metadata defined at the top of the Python file.

## 🚀 Usage

### Option 1 — using `uv run`

Clone the repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Run the program:

```bash
uv run speed_test.py https://example.com/file.jpg
```

By default, the program performs **10 sequential requests**.

### Change the number of requests

You can change the number of iterations using `-n` or `--iterations`:

```bash
uv run speed_test.py https://example.com/file.jpg -n 20
```

or:

```bash
uv run speed_test.py https://example.com/file.jpg --iterations 20
```

## 📋 Example

```bash
uv run speed_test.py https://example.com/large-file.zip
```

Example output:

```text
🚀 Starting speed test for: https://example.com/large-file.zip
🔄 10 sequential requests will be performed...

[01/10] ⏱️ 1.284 sec | 📦 25.00 MB | ⚡️ 19.47 MB/s
[02/10] ⏱️ 1.190 sec | 📦 25.00 MB | ⚡️ 21.01 MB/s
[03/10] ⏱️ 1.231 sec | 📦 25.00 MB | ⚡️ 20.31 MB/s
...
[10/10] ⏱️ 1.205 sec | 📦 25.00 MB | ⚡️ 20.75 MB/s

=============================================
📊 FINAL RESULTS:
📥 Total downloaded:       250.00 MB
⏱️ Average request time:   1.221 sec
⚡️ Average speed:          20.47 MB/s (Megabytes/sec)
=============================================
```

## 🧠 How it works

For every request, the program:

1. Records the start time.
2. Sends an HTTP GET request.
3. Checks the HTTP response status.
4. Downloads the response in **64 KB chunks**.
5. Counts the received bytes.
6. Measures the total download time.
7. Calculates the download speed:

```text
speed = amount of data / elapsed time
```

After all requests are completed, the program calculates the average values:

```text
average time = total time / number of requests
```

```text
average speed = total downloaded data / total time
```

## 📦 Why `stream=True` is used

Instead of loading the entire file into memory, the program downloads the response in chunks:

```python
requests.get(url, stream=True)
```

The response is then processed block by block:

```python
for chunk in response.iter_content(chunk_size=65536):
    downloaded_bytes += len(chunk)
```

This makes it possible to test large files without keeping the entire file in RAM.

## ⚠️ Important notes

The measured result depends on more than just your internet connection.

The measurement can be affected by:

- the server hosting the file;
- distance to the server;
- server load;
- CDN;
- network routing;
- VPN or proxy;
- Wi-Fi instead of Ethernet;
- other applications or devices using the network.

For more consistent results, use a relatively large file hosted on a fast and stable server.

All dependencies are declared directly inside `speed_test.py` using the `uv` script metadata format.
