import os_module_operation
import replace_fullname_to_n


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
