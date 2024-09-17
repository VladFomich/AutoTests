# Задание 2. (повышенной сложности)

# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, 
# в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять 
# из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.

import subprocess
import string


def is_command_successful(command, text_to_find):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')

    translator = str.maketrans("", "", string.punctuation)
    output_words = result.stdout.translate(translator).split()
    print(output_words)
    return text_to_find in output_words


command_example_words = "echo 'Home work 2!'"
text_example_words = "work"
result_words = is_command_successful(command_example_words, text_example_words)

print(result_words)