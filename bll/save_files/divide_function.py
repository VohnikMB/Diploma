"""
Файл що містить функції для неймінгу і розподілу данних

Функції:
    - divide_data: Розділяє дані на фрагменти.
    - divide_files_name: Генерує імена для розділених файлів на основі хеш-типу, кількості фрагментів та імені первинного файлу.

"""


def divide_data(decrypted_data, fragments):
    data = []
    length = len(decrypted_data)
    fragment_size = length // fragments
    remainder = length % fragments  # Для розподілу залишку

    start_index = 0
    for i in range(fragments):
        end_index = start_index + fragment_size + (1 if i < remainder else 0)
        data.append(decrypted_data[start_index:end_index])
        start_index = end_index

    return data


def divide_files_name(fragments, hash_type, file_name):
    hash_in_name = None
    match hash_type:
        case "sha512":
            hash_in_name = "sh"
        case "BLAKE2b":
            hash_in_name = "b2"
        case "salt":
            hash_in_name = "ss"
    names = []
    for i in range(fragments):
        names.append(hash_in_name + str(i) + str(fragments) + str(file_name) + "_")

    return names
