import os


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


def print_path_to_current_directory():
    print(f"Путь до текущей директории:\n{os.getcwd()}\n")


if __name__ == '__main__':
    print_os_name()
    print_path_to_current_directory()
