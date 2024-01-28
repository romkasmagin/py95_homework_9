START_FILE = "some_text_for_third_task"
RESULT_FILE = "result_text_for_third_task"


def work_with_file(start_file, result_file):
    with open(start_file, 'r') as file_reader:
        with open(result_file, 'w') as file_writer:
            for lines in file_reader:
                line = lines.strip()
                if line:
                    word, counter = count_word_in_lines(line)
                    file_writer.write(f"{word} - {counter}\n")


def count_word_in_lines(line):
    words = line.split()
    words_and_counter_in_string = dict()

    for word in words:
        if word in words_and_counter_in_string:
            words_and_counter_in_string[word] += 1
        else:
            words_and_counter_in_string[word] = 1

    max_word_in_line = max(words_and_counter_in_string,
                           key=words_and_counter_in_string.get)

    return max_word_in_line, words_and_counter_in_string[max_word_in_line]


def start_program():
    work_with_file(START_FILE, RESULT_FILE)

