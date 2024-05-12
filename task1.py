

import os
import shutil
import argparse

def copy_files(source_dir, destination_dir):

    # Перевірка існування директорії призначення
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Рекурсивний обхід директорій та копіювання файлів
    for root, dirs, files in os.walk(source_dir):
        for name in files:
            source_file_path = os.path.join(root, name)
            destination_subdir = os.path.join(destination_dir, os.path.splitext(name)[1][1:])
            destination_file_path = os.path.join(destination_subdir, name)

            # Створення піддиректорії за розширенням, якщо вона ще не існує
            if not os.path.exists(destination_subdir):
                os.makedirs(destination_subdir)

            try:
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Файл {name} скопійовано до {destination_subdir}")
            except Exception as e:
                print(f"Помилка копіювання файлу {name}: {e}")

def main():
    
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Копіювання файлів та сортування за розширенням.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    args = parser.parse_args()

    # Виклик рекурсивної функції копіювання файлів
    copy_files(args.source_dir, args.destination_dir)

if __name__ == "__main__":
    main()



