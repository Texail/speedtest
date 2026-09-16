# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests",
# ]
# ///

import requests
import time
import argparse
import sys

def measure_speed(url: str, iterations: int = 10):
    total_time = 0.0
    total_bytes = 0

    print(f"🚀 Начинаем замер скорости для: {url}")
    print(f"🔄 Будет выполнено {iterations} последовательных запросов...\n")

    for i in range(1, iterations + 1):
        start_time = time.perf_counter()

        try:
            # stream=True позволяет читать данные по частям, не перегружая RAM
            with requests.get(url, stream=True, timeout=60) as response:
                response.raise_for_status()
                
                downloaded_bytes = 0
                # Читаем чанками по 64 КБ
                for chunk in response.iter_content(chunk_size=65536):
                    downloaded_bytes += len(chunk)

            end_time = time.perf_counter()
            elapsed = end_time - start_time
            
            total_time += elapsed
            total_bytes += downloaded_bytes

            mb_downloaded = downloaded_bytes / (1024 * 1024)
            current_speed = mb_downloaded / elapsed if elapsed > 0 else 0
            
            print(f"[{i:02d}/{iterations}] ⏱️ {elapsed:.3f} сек | 📦 {mb_downloaded:.2f} MB | ⚡️ {current_speed:.2f} MB/s")

        except requests.exceptions.RequestException as e:
            print(f"\n❌ Ошибка при запросе {i}: {e}")
            sys.exit(1)

    # Итоговые вычисления
    avg_time = total_time / iterations
    total_mb = total_bytes / (1024 * 1024)
    avg_speed = total_mb / avg_time if avg_time > 0 else 0

    print("\n" + "="*45)
    print("📊 ИТОГОВЫЕ РЕЗУЛЬТАТЫ:")
    print(f"📥 Всего скачано:          {total_mb:.2f} MB")
    print(f"⏱️ Среднее время запроса:  {avg_time:.3f} сек")
    print(f"⚡️ Средняя скорость:       {avg_speed:.2f} MB/s (Мегабайт/с)")
    print("="*45)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Утилита для замера скорости скачивания.")
    parser.add_argument("url", help="Ссылка на тяжелый файл (например, картинку или архив)")
    parser.add_argument("-n", "--iterations", type=int, default=10, help="Количество запросов (по умолчанию 10)")
    
    args = parser.parse_args()
    measure_speed(args.url, args.iterations)