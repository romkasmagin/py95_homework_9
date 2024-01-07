import os
# Для получения файлов соответствующих заданному шаблону.
from glob import glob


# Словарь, хранящий в себе все расширения в виде ключей, а имена папок
# ввиде значений. Является конфигурационным словарем. Можно настраивать.
# Для сортировки файлов с расширениями по соответсвующимся папкам.
extensions = {
    'jpg': 'images',
    'png': 'images',
    'ico': 'images',
    'gif': 'images',
    'svg': 'images',
    'sql': 'sql',
    'sqlite3': 'sql',
    'msi': 'programs',
    'exe': 'programs',
    'pdf': 'pdf',
    'rar': 'archive',
    'zip': 'archive',
    'gz': 'archive',
    'tar': 'archive',
    'txt': 'text',
    'torrent': 'torrent',
    'mp3': 'audio',
    'wav': 'audio',
    'mp4': 'video',
    'webm': 'video',
    'json': 'json',
    'css': 'web',
    'js': 'web',
    'html': 'web',
    'apk': 'apk',
}


def print_os_name() -> None:
    """
    Данная функция создает объект класса os.uname,
    затем выводит следующие поля класса:
    :keyword:
    machine: Архитектура вашего компьютера.

    sysname: Название операционной системы вашего компьютера.

    release: Релизная версия, установленная на вашем компьютере.
    """
    os_info = os.uname()
    print(f'Архитектура компьютера: {os_info.machine}\n'
          f'Имя системы: {os_info.sysname}\n'
          f'Релиз системы: {os_info.release}\n')


def print_path_to_current_directory() -> None:
    print(f"Путь до текущей директории:\n{os.getcwd()}\n")


def sort_file_by_extension():
    """
    Функция просматривает все файлы в текущей директории,
    перемещает файлы в соответсвующие расширениям файлов директории,
    ксли таковых нет, то создает их.
    """
    path = os.getcwd()
    if extensions:
        for extension, folder_name in extensions.items():
            # При помощи модуля glob получаем все файлы в текущей
            # директории с расширением {extension}.
            files = glob(f"*.{extension}")

            if len(files):
                print(f"[?] Найдено {len(files)} файла(-ов)"
                      f" с расширением {extension}")

            if not os.path.isdir(os.path.join(path,folder_name)) and files:
                os.mkdir(os.path.join(path, folder_name))
                print(f"[+] Создана папка {folder_name}.")

            for file in files:
                # Хранится информация
                # о расположении файла в данный момент.
                basename = os.path.basename(file)
                extension_folder = os.path.join(path, folder_name, basename)
                print(f"[*] Перенесён файл '{file}' в '{extension_folder}'")
                os.replace(file, extension_folder)


def get_size_folder():
    path = os.getcwd()
    files = os.listdir()

    for folder_name in extensions.values():
        if folder_name in files:
            print(f"В папке '{folder_name}' находится "
                  f"{len(os.listdir(os.path.join(folder_name)))} файлов"
                  f"общим размером {os.stat(folder_name).st_size}.")


def rename_test_in_hello():
    path = os.getcwd()
    file = os.path.join(path, 'text')
    old_file_name = os.path.join(file, 'test.txt')
    new_file_name = os.path.join(file, 'hello.txt')
    if os.path.exists(old_file_name):
        os.rename(old_file_name, new_file_name)
        print("Файл 'test.txt' был переименован в 'hello.txt'")


if __name__ == '__main__':
    print_os_name()
    print_path_to_current_directory()
    sort_file_by_extension()
    get_size_folder()
    rename_test_in_hello()
