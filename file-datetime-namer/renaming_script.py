import os
import datetime

def rename_files_with_unique_names_using_dict():
    print(f'Directory "{directory_path}"')

    for filename in os.listdir(directory_path):
    directory_path = os.getcwd()
    script_name = 'renaming_script.py'
    batch_name = 'run_script.bat'
    renamed_files = {}  # Dictionary to track renamed files

        file_path = os.path.join(directory_path, filename)
        if (filename == script_name) or (filename == batch_name) or not os.path.isfile(file_path):
            continue

        file_time = os.path.getctime(file_path)
        date_time = datetime.datetime.fromtimestamp(file_time)
        date_time_str = date_time.strftime('%Y%m%d_%H%M%S')

        new_filename = f"{date_time_str}{os.path.splitext(filename)[1]}"
        counter = 1
        # Check the dictionary for existing file name and modify if necessary
        while new_filename in renamed_files:
            new_filename = f"{date_time_str}_{counter}{os.path.splitext(filename)[1]}"
            counter += 1
        # Проблематика використання:
        # наприклад є файли 112233 112233_1, 112233_2, 112233_3, 112233_4
        # Якщо перейменувати якийсь з цих файлів, окрім останнього, на назву Х, то виникне помилка при запуску
        # скрипта для такого набору даних. Причина в тому що скрипт намагається перейменувати файл в уже існуючий файл
        # з такою ж самою назвою.
        # Проста перевірка на те чи є такий файл в директорії не допомагає, оскільки немає гарантії чи ми не знайдемо в
        # в директорії цей самий файл який і перейменовуємо.
        # Перейменувати сам поточний файл в таке саме ім'я - ОК.
        # Перейменувати поточний файл в ім'я файлу який вже існує в цій директорії - НЕ ОК.
        # Вирішується - перейменуванням файлу який викликав таку колізію
        # Можна перейменувати всі файли за зростаючими числами 1,2,3,4,5. А потім перейменувати за унікальними датами створення.
        #while os.path.exists(os.path.join(directory_path, new_filename)):
        #    new_filename = f"{date_time_str}_{counter}{os.path.splitext(filename)[1]}"
        #    counter += 1

        # Add the unique file name to the dictionary
        renamed_files[new_filename] = True
        new_file_path = os.path.join(directory_path, new_filename)
        os.rename(file_path, new_file_path)
        print(f'Renamed "{filename}" to "{new_filename}"')

    print('All files have been renamed with unique names.')

rename_files_with_unique_names_using_dict()