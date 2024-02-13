import json
import csv

import os_module_operation
import replace_fullname_to_n


# json_task
def read_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data


def write_csv(file_name, data):
    with open(file_name, 'w',  newline='',) as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())


def add_employee_json(file_name,
                      name,
                      birthday,
                      height,
                      weight,
                      car,
                      languages):
    data = read_json(file_name)
    new_employee = {
        'name': name,
        'birthday': birthday,
        'height': height,
        'weight': weight,
        'car': car,
        'languages': languages
    }
    data.append(new_employee)
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def add_employee_csv(file_name,
                     name,
                     birthday,
                     height,
                     weight,
                     car,
                     languages):
    data = read_json(file_name)
    new_employee = {
        'name': name,
        'birthday': birthday,
        'height': height,
        'weight': weight,
        'car': car,
        'languages': languages
    }
    data.append(new_employee)
    write_csv(file_name, data)


def get_info(file_name, name):
    data = read_json(file_name)

    for employee in data:
        if employee['name'] == name:
            print(f"Имя: {employee['name']}")
            print(f"Дата рождения: {employee['birthday']}")
            print(f"Рост: {employee['height']}")
            print(f"Вес: {employee['weight']}")
            print(f"Наличие автомобиля: {employee['car']}")
            print(f"Языки программирования: {employee['languages']}")
            # Для вызода из функции при нахождении сотрудника,
            # если не нашли, то отработает print за телом for.
            return
    print("Сотрудник с указанным именем не найден.")


def filter_by_language(file_name, programming_language):
    data = read_json(file_name)

    filtered_employees = list()
    for employee in data:
        if programming_language in employee['languages']:
            filtered_employees = filtered_employees.append(employee)

    if filtered_employees:
        print(f"Сотрудники, владеющие языком программирования "
              f"{programming_language}:")
        for employee in filtered_employees:
            print(f"Имя: {employee['name']}, "
                  f"языки программирования: {employee['languages']}")
    else:
        print(f"Нет сотрудников, владеющих языком программирования "
              f"{programming_language}.")


def filter_by_birth_year(file_name, birth_year):
    data = read_json(file_name)
    filtered_employees = [
        employee for employee in data
        if int(employee['birthday'].split('.')[2]) < birth_year
    ]
    if filtered_employees:
        print("Сотрудники, у которых год рождения меньше заданного:")
        for employee in filtered_employees:
            print(f"Имя: {employee['name']}, рост: {employee['height']}")

        heights = [employee['height'] for employee in filtered_employees]
        average_height = sum(heights) / len(heights)
        print("Средний рост сотрудников, у которых год рождения меньше",
              birth_year, ":", average_height)
    else:
        print("Нет сотрудников с годом рождения меньше", birth_year)


def menu():
    file_employee = 'json_task/employees.json'
    while True:
        print("Меню:")
        print("1. Чтение данных из JSON и преобразование в CSV")
        print("2. Сохранение данных в CSV")
        print("3. Добавление нового сотрудника в JSON")
        print("4. Добавление нового сотрудника в CSV")
        print("5. Вывод информации о сотруднике по имени")
        print("6. Фильтрация сотрудников по языку программирования")
        print("7. Фильтрация сотрудников по году рождения")
        print("8. Выход")

        choice = int(input("Выберите действие (1-8): "))

        match choice:
            case 1:
                data = read_json(file_employee)
                write_csv('output.csv', data)
                print("Данные успешно преобразованы в CSV.")
            case 2:
                data = read_json(file_employee)
                write_csv('output.csv', data)
                print("Данные успешно сохранены в CSV.")
            case 3:
                name = input("Имя сотрудника: ")
                birthday = input("Дата рождения сотрудника (ДД.ММ.ГГГГ): ")
                while True:
                    parts = birthday.split(".")
                    if len(parts) != 3 or \
                            not all(part.isdigit() for part in parts):
                        print("Некорректный формат даты. "
                              "Попробуйте еще раз.")
                        birthday = input("Дата рождения сотрудника"
                                         " (день.месяц.год): ")
                        continue

                    day, month, year = map(int, parts)
                    if day < 1 or day > 31 or month < 1\
                            or month > 12 or year < 0:
                        print("Некорректная дата. Попробуйте еще раз.")
                        birthday = input("Дата рождения сотрудника "
                                         "(день.месяц.год): ")
                        continue
                    break

                state = True
                while state:
                    height = input("Рост сотрудника: ")
                    if height.isdigit() and int(height) > 0:
                        height = int(height)
                        state = False
                    else:
                        print("Некорректный ввод роста. Попробуйте еще раз.")

                state = True
                while state:
                    weight = input("Вес сотрудника: ")
                    if weight.isdigit() and int(weight) > 0:
                        weight = int(weight)
                        state = False
                    else:
                        print("Некорректный ввод веса. Попробуйте еще раз.")

                car_input = input("Есть ли у сотрудника машина (True/False): ")
                while car_input.lower() not in ['true', 'false']:
                    print("Некорректный ввод. Попробуйте еще раз.")
                    car_input = input("Есть ли у сотрудника "
                                      "машина (True/False): ")

                car = bool(car_input)

                languages_input = input("Язык программирования "
                                        "(через запятую): ")
                languages = [
                    lang.strip() for lang in languages_input.split(",")
                ]

                add_employee_json(file_employee,
                                  name,
                                  birthday,
                                  height,
                                  weight,
                                  car,
                                  languages)
                print("Новый сотрудник успешно добавлен в JSON.")
            case 4:
                name = input("Имя сотрудника: ")
                birthday = input("Дата рождения сотрудника (ДД.ММ.ГГГГ): ")
                while True:
                    parts = birthday.split(".")
                    if len(parts) != 3 or \
                            not all(part.isdigit() for part in parts):
                        print("Некорректный формат даты. Попробуйте еще раз.")
                        birthday = input("Дата рождения сотрудника"
                                         " (день.месяц.год): ")
                        continue

                    day, month, year = map(int, parts)
                    if day < 1 or day > 31 or month < 1 \
                            or month > 12 or year < 0:
                        print("Некорректная дата. Попробуйте еще раз.")
                        birthday = input("Дата рождения сотрудника "
                                         "(день.месяц.год): ")
                        continue
                    break

                state = True
                while state:
                    height = input("Рост сотрудника: ")
                    if height.isdigit() and int(height) > 0:
                        height = int(height)
                        state = False
                    else:
                        print("Некорректный ввод роста. Попробуйте еще раз.")

                state = True
                while state:
                    weight = input("Вес сотрудника: ")
                    if weight.isdigit() and int(weight) > 0:
                        weight = int(weight)
                        state = False
                    else:
                        print("Некорректный ввод веса. Попробуйте еще раз.")

                car_input = input("Есть ли у сотрудника машина (True/False): ")
                while car_input.lower() not in ['true', 'false']:
                    print("Некорректный ввод. Попробуйте еще раз.")
                    car_input = input("Есть ли у сотрудника"
                                      " машина (True/False): ")

                car = bool(car_input)

                languages_input = input("Язык программирования"
                                        " (через запятую): ")
                languages = [lang.strip() for lang in
                             languages_input.split(",")]

                add_employee_csv(file_employee,
                                 name,
                                 birthday,
                                 height,
                                 weight,
                                 car,
                                 languages)
                print("Новый сотрудник успешно добавлен в CSV.")
            case 5:
                input_name = input("Введите имя сотрудника: ")
                get_info(file_employee, input_name)
            case 6:
                input_language = input("Введите язык программирования: ")
                filter_by_language(file_employee, input_language)
            case 7:
                year = int(input("Введите год рождения: "))
                filter_by_birth_year(file_employee, year)
            case 8:
                print("Выход из программы.")
                break
            case _:
                print("Некорректный выбор. "
                      "Пожалуйста, выберите действие от 1 до 8.")


if __name__ == '__main__':
    print("В данной программе будет продемонстрировано "
          "выполнение домашнего задания под номером девять.\n"
          "Данное решение размещено на GitHub.\n"
          "Его можно скачать "
          # ДОБАВИТЬ SSH token после размещения на GitHub!!!
          "по следующему SSH(Необходим public SSH key):\n"
          u"\n"
          "Или воспользуйтесь следующим https:\n"
          u"")

    os_module_operation.print_os_name()
    os_module_operation.print_path_to_current_directory()
    os_module_operation.sort_file_by_extension()
    os_module_operation.get_size_folder()
    os_module_operation.rename_test_in_hello()

    input('Первое задание отработало, для продолжение нажмите Enter...')

    print('Второе задание заменит ФИО на N')
    text = input('Введите текст судебного документа: ')
    replace_fullname_to_n.replace_fullname_to_n(text)

    menu()
